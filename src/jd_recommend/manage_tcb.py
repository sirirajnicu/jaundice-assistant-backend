from src.jd_models import Patient, Gender
from src.jd_models.treatment import TreatmentType, generate_treatment_msgs
from typing import List


def tcb_within_lt3_geq15_from_threshold(tcb_value: float,
                                        photo_threshold: float) -> bool:
    threshold_diff = photo_threshold - tcb_value
    return threshold_diff <= 3.0 or tcb_value >= 15.0


def handle_tcb_lt_photo_threshold(patient: Patient,
                                  photo_threshold: float) -> List[TreatmentType]:
    treatments: List[TreatmentType] = []
    if tcb_within_lt3_geq15_from_threshold(patient.tcb_value[-1].data, photo_threshold):
        treatments.append(TreatmentType.TSB_THEN_CONSULT)

    elif (patient.change_rate_first_day() > 0.3 or
            patient.change_rate_after_first_day() > 0.2 or
            patient.had_jaundice_within_first_24hrs()):
        treatments.extend([
            TreatmentType.TSB_THEN_CONSULT,
            TreatmentType.WORK_UP
        ])
        if patient.gender == Gender.MALE:
            treatments.append(TreatmentType.G6PD)

    else:
        treatments.append(TreatmentType.TCB_WITH_TIMING)

    return treatments


def handle_tcb_geq_photo_threshold(patient: Patient,
                                   blood_threshold: float) -> List[TreatmentType]:
    diff_from_threshold = patient.tcb_value[-1].data - blood_threshold

    if diff_from_threshold < -2.0:
        treatments: List[TreatmentType] = [
            TreatmentType.TSB_THEN_CONSULT,
            TreatmentType.WORK_UP,
        ]
        if patient.gender == Gender.MALE:
            treatments.append(TreatmentType.G6PD)
        return treatments

    else:
        treatments: List[TreatmentType] = [
            TreatmentType.TO_EMERGENCY,
            TreatmentType.DOUBLE_PHOTO,
            TreatmentType.RUSHED_BLOOD_TEST,
            TreatmentType.TB_DB_ALBUMIN,
            TreatmentType.WORK_UP,
            TreatmentType.PROVIDE_ELECTROLYTES,
            TreatmentType.GROUP_MATCH_AND_PREP_TRANSFUSION,
            TreatmentType.NPO_AND_PERIPHERAL_IV,
            TreatmentType.NPO_CENTRAL
        ]
        if patient.gender == Gender.MALE:
            treatments.append(TreatmentType.G6PD)
        return treatments


# TODO: change return type to a treatment class
def recommend_from_tcb(patient: Patient,
                       photo_threshold: float,
                       blood_threshold: float) -> List[str]:
    """
    Based on Figure 1: Management after obtaining TCB results
    """
    if patient is None or len(patient.tcb_value) <= 0:
        raise ValueError("Invalid Patient object")

    treatments: List[TreatmentType] = []
    if patient.tcb_value[-1].data < photo_threshold:
        treatments.extend(handle_tcb_lt_photo_threshold(patient, photo_threshold))
    else:
        treatments.extend(handle_tcb_geq_photo_threshold(patient, blood_threshold))

    return generate_treatment_msgs(treatments, patient)
