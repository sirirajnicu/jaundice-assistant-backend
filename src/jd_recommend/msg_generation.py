from typing import List
from src.jd_models import Patient, TreatmentType, BASE_MSG_DB
from follow_up_after_off_photo import manage_follow_up_after_off_photo
from follow_up_never_on_photo import manage_follow_up_never_on_photo, BilirubinType


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
                ...
        return BASE_MSG_DB[treatment] + timing

    return [generate_treatment_msg(tt) for tt in tts]
