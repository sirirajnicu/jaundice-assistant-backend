from src.jd_models import Patient, PhototherapyType
from src.jd_models.treatment import TreatmentType, generate_treatment_msgs
from typing import List


def handle_far_below_threshold(patient: Patient) -> List[TreatmentType]:
    """
    Based on Figure 4 - left arm
    """
    treatments: List[TreatmentType] = [
        TreatmentType.TSB_SHIELDED_TCB_BY_RISK,
        TreatmentType.PE,
        TreatmentType.WORK_UP,
    ]

    if len(patient.photo_therapy_record) > 0:
        match patient.photo_therapy_record[-1].data:
            case PhototherapyType.NONE:
                treatments.append(TreatmentType.ON_PHOTO)
            case PhototherapyType.SINGLE:
                treatments.append(TreatmentType.DOUBLE_PHOTO)
            case PhototherapyType.DOUBLE:
                treatments.append(TreatmentType.INCR_PHOTO_INTENSITY)
    else:
        treatments.append(TreatmentType.ON_PHOTO)

    return treatments


# TODO: make a pop-up on user screen when this is called
def request_bind_score() -> float:
    return 0.0


def handle_close_below_threshold(patient: Patient) -> List[TreatmentType]:
    """
    Based on Figure 4 - middle arm
    """
    treatments: List[TreatmentType] = []
    if len(patient.photo_therapy_record) > 0:
        match patient.photo_therapy_record[-1].data:
            case PhototherapyType.NONE:
                treatments.append(TreatmentType.DOUBLE_PHOTO_STAT)
            case PhototherapyType.SINGLE:
                treatments.append(TreatmentType.DOUBLE_PHOTO)
            case PhototherapyType.DOUBLE:
                treatments.append(TreatmentType.INCR_PHOTO_INTENSITY)
    else:
        treatments.append(TreatmentType.DOUBLE_PHOTO_STAT)

    if request_bind_score() >= 4:
        treatments.append(TreatmentType.EXCHANGE_TRANSFUSION)
    else:
        treatments.extend([
            TreatmentType.CONT_PHOTO,
            TreatmentType.EXCHANGE_BY_BA_RATIO,
            TreatmentType.NPO_AND_PERIPHERAL_IV,
            TreatmentType.CROSS_MATCH,
            TreatmentType.PE,
            TreatmentType.WORK_UP,
            TreatmentType.TSB_2_HOURS,
            TreatmentType.IVIG,
        ])

    return treatments


def recommend_tsb_over_threshold(patient: Patient, exchange_threshold: float) -> List[str]:
    """
    Based on Figure 4: Managements of TSB levels that are exceeding phototherapy threshold
    """
    treatments: List[TreatmentType] = []
    tsb_diff = exchange_threshold - patient.tsb_value[-1].data

    if patient.tsb_value[-1].data >= exchange_threshold:
        treatments.extend([
            TreatmentType.DOUBLE_PHOTO_STAT,
            TreatmentType.EXCHANGE_TRANSFUSION,
            TreatmentType.NPO_CENTRAL,
            TreatmentType.CROSS_MATCH,
            TreatmentType.PE,
            TreatmentType.WORK_UP,
            TreatmentType.TSB_2_HOURS,
        ])
    elif tsb_diff > 2.0:
        treatments.extend(handle_far_below_threshold(patient))
    else:
        treatments.extend(handle_close_below_threshold(patient))

    return generate_treatment_msgs(treatments, patient)
