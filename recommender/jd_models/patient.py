from dataclasses import dataclass
from datetime import datetime, timedelta
from aenum import Enum
from typing import List, Tuple, TypeVar, Set

T = TypeVar("T")


@dataclass
class Record(Tuple[datetime, T]):
    time: datetime
    data: T


Records = List[Record[T]]

AdmissionType = Enum("AdmissionType", "BIRTH_ADMISSION READMISSION DISCHARGE")
Gender = Enum("Gender", "MALE FEMALE")
PhototherapyType = Enum("PhototherapyType", "NONE SINGLE DOUBLE")
NeurotoxicityRisk = Enum("NeurotoxicityRisk", "NO_RISK AT_RISK")
Threshold = Enum("Threshold", "PHOTO EXCHANGE")


def is_off_photo(record: Record[PhototherapyType]) -> bool:
    return record.data is PhototherapyType.NONE


@dataclass
class Patient:
    gender: Gender
    gestational_age: int
    birth_date_time: datetime

    neuro_risk: Set[NeurotoxicityRisk]

    tcb_value: Records[float]
    tsb_value: Records[float]
    albumin_value: Records[float]
    photo_therapy_record: Records[PhototherapyType]
    admission_record: Records[AdmissionType]

    # "getters"
    def age(self) -> timedelta:
        return datetime.now() - self.birth_date_time

    def age_at_start_of_photo(self) -> None or timedelta:
        if len(self.photo_therapy_record) <= 0:
            return None
        if self.photo_therapy_record[-1].data == PhototherapyType.NONE:
            return None

        return self.photo_therapy_record[-1].time - self.birth_date_time

    # conditions
    def has_hemolytic_diseases(self) -> bool:
        return False

    def had_photo_during_birth_admission(self) -> bool:
        if len(self.admission_record) < 1 or self.admission_record[0].data is not AdmissionType.BIRTH_ADMISSION:
            return False

        discharge_time = datetime.now() \
            if len(self.admission_record) < 2 or self.admission_record[1].data is not AdmissionType.DISCHARGE \
            else self.admission_record[1].time

        photo_during_birth_admission = [rec for rec in self.photo_therapy_record
                                        if rec.time <= discharge_time and rec.data is not PhototherapyType.NONE]
        return len(photo_during_birth_admission) > 0

    def had_jaundice_within_first_24hrs(self) -> bool:
        first_24hrs_values = self._first_24hrs_tcb()
        if first_24hrs_values is None or len(first_24hrs_values) <= 0:
            return False
        return first_24hrs_values[-1].data > 2

    # TCB/TSB change rate
    def _first_24hrs_tcb(self) -> Records[float] or None:
        if self.tcb_value is None or len(self.tcb_value) <= 0:
            return None

        def within_first_24hrs(data_time: Record[float]) -> bool:
            return data_time.time <= self.birth_date_time + timedelta(hours=24)

        values_to_use = self.tsb_value if self.tsb_value is not None else self.tcb_value
        return list(filter(within_first_24hrs, values_to_use))

    def _first_24hrs_tsb(self) -> Records[float] or None:
        if self.tsb_value is None or len(self.tsb_value) <= 0:
            return None

        def within_first_24hrs(data_time: Record[float]) -> bool:
            return data_time.time <= self.birth_date_time + timedelta(hours=24)

        values_to_use = self.tsb_value
        return list(filter(within_first_24hrs, values_to_use))

    @staticmethod
    def compute_rate_of_change(record: Records[float]):
        last: Record[float] = record[-1]
        second_last: Record[float] = record[-2]

        data_diff = last.data - second_last.data
        time_diff = last.time - second_last.time
        time_conversion_ratio = timedelta(hours=1) / time_diff

        return data_diff * time_conversion_ratio

    def change_rate_first_day(self) -> float or None:
        first_day_values = self._first_24hrs_tcb()
        if first_day_values is None or \
                len(first_day_values) < 2 or \
                first_day_values[-1].data >= 15:
            first_day_values = self._first_24hrs_tsb()

        if len(first_day_values) < 2:
            return None

        return self.compute_rate_of_change(first_day_values)

    def change_rate_after_first_day(self) -> float or None:
        values_to_use = self.tcb_value
        if values_to_use is None or \
                len(values_to_use) < 2 or \
                values_to_use[-1].data >= 15:
            values_to_use = self.tsb_value

        if len(values_to_use) < 2:
            return None

        return self.compute_rate_of_change(values_to_use)

    # phototherapy-related
    def is_between_photo_therapy(self) -> bool:
        if len(self.photo_therapy_record) <= 0:
            return False

        return not (self.photo_therapy_record[-1].data is PhototherapyType.NONE)

    def is_within_96hrs_after_phototherapy(self) -> bool:
        if len(self.photo_therapy_record) <= 0:
            return False
        if self.is_between_photo_therapy():
            return True

        last_off_photo: Record[PhototherapyType] = list(filter(is_off_photo, self.photo_therapy_record))[-1]
        return (not len(last_off_photo) <= 0) and \
            (datetime.now() - last_off_photo.time <= timedelta(hours=96))

    def compute_ba_ratio(self) -> float:
        return self.tsb_value[-1].data / self.albumin_value[-1].data

    @staticmethod
    def default():
        return Patient(
            gender=Gender.MALE,
            gestational_age=35,
            birth_date_time=datetime.now() - timedelta(days=2, seconds=60 * 60 * 3),
            neuro_risk=NeurotoxicityRisk.NO_RISK,
            tcb_value=[],
            tsb_value=[],
            albumin_value=[],
            photo_therapy_record=[],
            admission_record=[],
        )
