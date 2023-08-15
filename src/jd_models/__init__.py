from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum
from typing import List, Tuple, TypeVar

T = TypeVar("T")


@dataclass
class Record(Tuple[datetime, T]):
    time: datetime
    data: T


Records = List[Record[T]]


class AdmissionType(Enum):
    BIRTH_ADMISSION = 0
    READMISSION = 1


class Gender(Enum):
    MALE = 0
    FEMALE = 1


class PhototherapyType(Enum):
    NONE = 0
    SINGLE = 1
    DOUBLE = 2


class NeurotoxicityRisk(Enum):
    NO_RISK = 0
    AT_RISK = 2


class Threshold(Enum):
    PHOTO = 0
    EXCHANGE = 1


@dataclass
class Patient:
    gender: Gender
    gestational_age: int
    birth_date_time: datetime

    admission_type: AdmissionType

    tcb_value: Records[float]
    tsb_value: Records[float]

    photo_therapy_record: Records[float]
    on_photo_therapy: PhototherapyType

    neuro_risk: NeurotoxicityRisk

    def age(self) -> timedelta:
        return datetime.now() - self.birth_date_time

    def age_at_start_of_photo(self) -> None or timedelta:
        if self.photo_therapy_record is None:
            return None

        return self.photo_therapy_record[0].time - self.birth_date_time

    def has_hemolytic_diseases(self) -> bool:
        return False

    def had_photo_during_birth_admission(self) -> bool:
        return False

    @staticmethod
    def default():
        return Patient(
            Gender.MALE,
            35,
            datetime.now() - timedelta(days=2, seconds=60 * 60 * 3),
            [],
            [],
            None,
            PhototherapyType.SINGLE,
            NeurotoxicityRisk.NO_RISK
        )
