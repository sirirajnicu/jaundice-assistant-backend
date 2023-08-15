from src.jd_models import Patient, Gender
from recommend_utils import tcb_within_lt3_geq15_from_threshold, \
    compute_first_day_tcb, \
    compute_later_tcb, \
    jx_within_first_24


def handle_tcb_lt_photo_threshold(patient: Patient,
                                  photo_threshold: float) -> str or list[str]:
    if tcb_within_lt3_geq15_from_threshold(patient.tcb_value[-1].data, photo_threshold):
        return "Conduct TSB and consult Clinician"

    if (compute_first_day_tcb(patient) > 0.3 or
            compute_later_tcb(patient) > 0.2 or
            jx_within_first_24(patient)):
        treatments = [
            "TSB + consult clinician",
            "CBC, blood smear, reti count if never been tested",
            "Blood group, DAT if never been tested",
        ]
        if patient.gender == Gender.MALE:
            treatments.append("G6PD assay if never been tested")
        return treatments

    else:
        return "Follow up with TCB"


def handle_tcb_geq_photo_threshold(patient: Patient,
                                   blood_threshold: float) -> str or list[str]:
    diff_from_threshold = patient.tcb_value[-1].data - blood_threshold

    if diff_from_threshold < -2.0:
        treatments = [
            "TSB + consult clinician",
            "CBC, blood smear, reti count if never been tested",
            "Blood group, DAT if never been tested",
        ]
        if patient.gender == Gender.MALE:
            treatments.append("G6PD assay if never been tested")
        return treatments

    else:
        treatments = [
            "Admit to emergency neonatal units to apply phototherapy",
            "Double phototherapy",
            "Blood test after admission and request for a rushed result",
            "TB/DB, albumin",
            "CBC, blood smear, reti count if never been tested",
            "Provide electrolytes if patient shows sign of dehydration",
            "Blood group, DAT if never been tested",
            "Group match and prepare for exchange transfusion after seeing TB/DB results",
            "NPO and provide IV",
            "Consult with a newborn fellow for considering doing a central line as they see fit"
        ]
        if patient.gender == Gender.MALE:
            treatments.append("G6PD assay if never been tested")
        return treatments


# TODO: change return type to a treatment class
def recommend_from_tcb(patient: Patient,
                       photo_threshold: float,
                       blood_threshold: float) -> str or list[str]:
    """
    Based on Figure 1: Management after obtaining TCB results
    """
    if patient is None or len(patient.tcb_value) <= 0:
        raise ValueError("Invalid Patient object")

    if patient.tcb_value[-1].data < photo_threshold:
        return handle_tcb_lt_photo_threshold(patient, photo_threshold)
    else:
        return handle_tcb_geq_photo_threshold(patient, blood_threshold)
