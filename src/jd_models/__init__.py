from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum
from typing import Tuple


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


StartEndTime = Tuple[datetime, datetime]


@dataclass
class Patient:
    gender: Gender
    gestational_age: int
    birth_date_time: datetime

    tcb_value: list[float]
    tsb_value: list[float]

    photo_therapy_timing: StartEndTime or None
    on_photo_therapy: PhototherapyType

    neuro_risk: NeurotoxicityRisk

    def age(self) -> timedelta:
        return datetime.now() - self.birth_date_time

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
