from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from numpy import ndarray

Gender = Enum("Gender", ["MALE", "FEMALE"])


@dataclass
class Patient:
    gender: Gender
    gestational_age: int
    birth_date_time: datetime

    tcb_value: ndarray
    tsb_value: ndarray
