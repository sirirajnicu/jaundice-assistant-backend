from src.jd_models import Patient, Gender
from recommend_utils import tcb_within_lt3_geq15_from_threshold, \
    compute_first_day_tcb, \
    compute_later_tcb, \
    jx_within_first_24


def handle_tcb_lt_photo_threshold(patient: Patient,
                                  photo_threshold: float) -> str or list[str]:
    if tcb_within_lt3_geq15_from_threshold(patient.tcb_value, photo_threshold):
        return "Conduct TSB and consult Clinician"

    elif (compute_first_day_tcb(patient) > 0.3 or
          compute_later_tcb(patient) > 0.2 or
          jx_within_first_24(patient)):
        treatments = [
            "TSB + consult clinician",
            "CBC, blood smear, reti count",
            "Blood group, DAT",
        ]
        if patient.gender == Gender.MALE:
            treatments.append("G6PD")
        return treatments

    else:
        return "Follow up with TCB"


def handle_tcb_geq_photo_threshold(patient: Patient,
                                   blood_threshold: float) -> str or list[str]:
    diff_from_threshold = patient.tcb_value - blood_threshold

    if diff_from_threshold < -2.0:
        treatments = [
            "TSB + consult clinician",
            "CBC, blood smear, reti count",
            "Blood group, DAT",
        ]
        if patient.gender == Gender.MALE:
            treatments.append("G6PD")
        return treatments

    else:
        treatments = [
            "Admit to emergency neonatal units",
            "Double phototherapy",
            "TB/DB, albumin, CBC, blood smea, reti count",
            "Blood group, DAT",
            "Group match",
        ]
        if patient.gender == Gender.MALE:
            treatments.append("G6PD")
        return treatments


# TODO: change return type to a treatment class
def recommend_from_tcb(patient: Patient,
                       photo_threshold: float,
                       blood_threshold: float) -> str or list[str]:
    if patient is None or len(patient.tcb_value) <= 0:
        raise ValueError("Invalid Patient object")

    if patient.tcb_value[-1] < photo_threshold:
        return handle_tcb_lt_photo_threshold(patient, photo_threshold)
    else:
        return handle_tcb_geq_photo_threshold(patient, blood_threshold)
