from typing import List
from recommender.jd_models import Patient, TreatmentType, BASE_MSG_DB
from follow_up_after_off_photo import manage_follow_up_after_off_photo
from follow_up_never_on_photo import manage_follow_up_never_on_photo, BilirubinType


def compute_exchange_threshold_by_ba_ratio(patient: Patient) -> float:
    match patient.gestational_age >= 38 and len(patient.neuro_risk) >= 1:
        case True, True:
            return 7.2
        case True, False:
            return 8.0
        case False, True:
            return 6.8
        case False, False:
            return 7.2


def manage_exchange_by_ba_ratio(patient: Patient) -> str:
    ba_ratio = patient.compute_ba_ratio()
    exchange_threshold = compute_exchange_threshold_by_ba_ratio(patient)

    if ba_ratio >= exchange_threshold:
        return "Consider exchange transfusion"
    return ""


def generate_treatment_msgs(tts: List[TreatmentType],
                            patient: Patient,
                            photo_threshold: float = 0.0,
                            bilirubin_type: BilirubinType = BilirubinType.TSB) -> List[str]:
    def generate_treatment_msg(treatment: TreatmentType) -> str:
        timing = ""
        match treatment:
            case TreatmentType.TCB_WITH_TIMING:
                timing = manage_follow_up_never_on_photo(patient, photo_threshold, bilirubin_type)
            case TreatmentType.TCSB_WITH_TIMING:
                timing = manage_follow_up_after_off_photo(patient)
            case TreatmentType.OFF_PHOTO_WITH_TIMING:
                timing = manage_follow_up_after_off_photo(patient)
            case TreatmentType.EXCHANGE_BY_BA_RATIO:
                timing = manage_exchange_by_ba_ratio(patient)
        return BASE_MSG_DB[treatment] + timing

    return [generate_treatment_msg(tt) for tt in tts]
