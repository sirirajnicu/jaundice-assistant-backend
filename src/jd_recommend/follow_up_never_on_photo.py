from src.jd_models import Patient
from datetime import timedelta
from enum import Enum


class BilirubinType(Enum):
    TCB = 0
    TSB = 1


def manage_follow_up_never_on_photo(patient: Patient, photo_threshold: float,
                                    bilirubin_type_to_check: BilirubinType) -> str:
    """
    Based on Figure 2: Management in the case that TCB/TSB is below phototherapy threshold during
    birth admission for infants >= 12 hours old who have never been on phototherapy
    """
    match bilirubin_type_to_check:
        case BilirubinType.TCB:
            b_difference = round(photo_threshold - patient.tcb_value[-1], 1)
        case BilirubinType.TSB:
            b_difference = round(photo_threshold - patient.tsb_value[-1], 1)
        case _:
            raise ValueError("Invalid bilirubin type")

    if b_difference <= 0:
        raise ValueError("Invalid TCB/TSB value")

    if 0.1 <= b_difference <= 1.9:
        if patient.age() < timedelta(hours=24):
            return "TCB in 4 to 8 hours"
        else:
            return "TCB in 4 to 24 hours"
    elif 2.0 <= b_difference <= 3.4:
        return "TCB in 4 to 24 hours"
    elif 3.5 <= b_difference <= 5.4:
        return "Can D/C TCB in 1 to 2 days"
    elif 5.5 <= b_difference <= 6.9:
        if patient.age() < timedelta(hours=72):
            return "Can D/C TCB in 2 days"
        else:
            # TODO: fix this to be automated
            return "Can D/C based on risk of box 1 and 2: " + \
                "1 week if any, otherwise 1 month"
    else:
        if patient.age() < timedelta(hours=72):
            return "Can D/C TCB in 3 days"
        else:
            # TODO: fix this to be automated
            return "Can D/C based on risk of box 1 and 2: " + \
                "1 week if any, otherwise 1 month"
