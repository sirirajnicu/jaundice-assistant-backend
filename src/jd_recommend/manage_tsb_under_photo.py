from src.jd_models import Patient, PhototherapyType, Gender
from src.jd_models.treatment import TreatmentType, generate_treatment_msg
from typing import List


def handle_tsb_lt_threshold_with_photo(patient: Patient,
                                       photo_threshold: float) -> List[TreatmentType]:
    """
    Based on Figure 3 - left arm
    """
    tsb_diff = photo_threshold - patient.tsb_value[-1].data
    treatments: List[TreatmentType] = []

    if tsb_diff < 2.0:
        treatments.extend([
            TreatmentType.CONT_PHOTO,
            TreatmentType.TSB_SHIELDED_TCB_BY_RISK,
        ])
    elif patient.photo_therapy_record[-1].data == PhototherapyType.SINGLE:
        treatments.append(TreatmentType.OFF_PHOTO_WITH_TIMING)
    else:
        treatments.extend([
            TreatmentType.TSB_SHIELDED_TCB_BY_RISK,
            TreatmentType.OFF_PHOTO_WITH_TIMING,
        ])

    return treatments


def handle_tsb_lt_threshold_no_photo(patient: Patient) -> List[TreatmentType]:
    """
    Based on Figure 3 - right arm
    """
    treatments: List[TreatmentType] = []
    if patient.is_within_96hrs_after_phototherapy():
        treatments.append(TreatmentType.TCSB_WITH_TIMING)  # follow up after off-photo

    elif (patient.change_rate_first_day() > 0.3 or
          patient.change_rate_after_first_day() > 0.2 or
          patient.had_jaundice_within_first_24hrs()):
        treatments.extend([
            TreatmentType.TSB_THEN_CONSULT,
            TreatmentType.WORK_UP,
        ])
        if patient.gender == Gender.MALE:
            treatments.append(TreatmentType.G6PD)

    else:
        treatments.append(TreatmentType.TCSB_WITH_TIMING)

    return treatments


def recommend_tsb_under_threshold(patient: Patient,
                                  photo_threshold: float) -> List[str]:
    """
    Based on Figure 3: Management of TSB levels that are below phototherapy threshold
    """
    treatments: List[TreatmentType] = []
    if patient.is_between_photo_therapy():
        treatments.extend(handle_tsb_lt_threshold_no_photo(patient))
    else:
        treatments.extend(handle_tsb_lt_threshold_with_photo(patient, photo_threshold))

    return generate_treatment_msg(treatments, patient)
