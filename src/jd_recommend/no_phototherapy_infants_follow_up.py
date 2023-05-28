from jd_models import Patient
from datetime import timedelta, now


def recommend_follow_up_tcb(patient: Patient, photo_threshold: float) -> str:
    tcb_difference = round(photo_threshold - patient.tcb_value, 1)
    patient_age = patient.birth_date_time - now()

    if tcb_difference <= 0:
        raise ValueError("Invalid TCB value")

    if 0.1 <= tcb_difference <= 1.9:
        if patient_age < timedelta(hours=24):
            return "TCB in 4 to 8 hours"
        else:
            return "TCB in 4 to 24 hours"
    elif 2.0 <= tcb_difference <= 3.4:
        return "TCB in 4 to 24 hours"
    elif 3.5 <= tcb_difference <= 5.4:
        return "Can D/C TCB in 1 to 2 days"
    elif 5.5 <= tcb_difference <= 6.9:
        if patient_age < timedelta(hours=72):
            return "Can D/C TCB in 2 days"
        else:
            # TODO: fix this to be automated
            return "Can D/C based on risk of box 1 and 2: " + \
                "1 week if any, otherwise 1 month"
    else:
        if patient_age < timedelta(hours=72):
            return "Can D/C TCB in 3 days"
        else:
            # TODO: fix this to be automated
            return "Can D/C based on risk of box 1 and 2: " + \
                "1 week if any, otherwise 1 month"
