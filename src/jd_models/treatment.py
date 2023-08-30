from aenum import AutoNumberEnum
from typing import Dict, List
from patient import Patient


class TreatmentType(AutoNumberEnum):
    WORK_UP = ()  # CBC, blood smear, reti count, blood group, DAT
    G6PD = ()
    TB_DB_ALBUMIN = ()
    PE = ()

    RUSHED_BLOOD_TEST = ()
    GROUP_MATCH_AND_PREP_TRANSFUSION = ()
    CROSS_MATCH = ()

    TSB_THEN_CONSULT = ()
    TSB_2_HOURS = ()
    TCB_WITH_TIMING = ()
    TSB_SHIELDED_TCB_BY_RISK = ()
    TCSB_WITH_TIMING = ()

    TO_EMERGENCY = ()

    ON_PHOTO = ()
    CONT_PHOTO = ()
    ON_SINGLE_WITH_TIMING = ()
    DOUBLE_PHOTO = ()
    DOUBLE_PHOTO_STAT = ()
    INCR_PHOTO_INTENSITY = ()
    OFF_PHOTO_WITH_TIMING = ()

    PROVIDE_ELECTROLYTES = ()
    NPO_AND_PERIPHERAL_IV = ()
    NPO_CENTRAL = ()
    IVIG = ()
    EXCHANGE_TRANSFUSION = ()
    EXCHANGE_BY_BA_RATIO_WITH_TIMING = ()


BASE_MSG_DB: Dict[TreatmentType, List[str]] = {
    # stores the base msg for each treatment type
}


def generate_treatment_msg(tts: List[TreatmentType], patient: Patient) -> List[str]:
    pass
