from aenum import AutoNumberEnum
from typing import Dict


class TreatmentType(AutoNumberEnum):
    WORK_UP = ()
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
    DOUBLE_PHOTO = ()
    DOUBLE_PHOTO_STAT = ()
    INCR_PHOTO_INTENSITY = ()
    OFF_PHOTO_WITH_TIMING = ()

    PROVIDE_ELECTROLYTES = ()
    NPO_AND_PERIPHERAL_IV = ()
    NPO_CENTRAL = ()
    IVIG = ()
    EXCHANGE_TRANSFUSION = ()
    EXCHANGE_BY_BA_RATIO = ()


BASE_MSG_DB: Dict[TreatmentType, str] = {
    TreatmentType.WORK_UP: "Conduct CBC, blood smear, and reti count, blood group, and DAT if not yet",
    TreatmentType.G6PD: "Conduct G6PD",
    TreatmentType.TB_DB_ALBUMIN: "TB/DB, albumin",
    TreatmentType.PE: "PE and work for causes",

    TreatmentType.RUSHED_BLOOD_TEST: "Rushed blood test after admission",
    TreatmentType.GROUP_MATCH_AND_PREP_TRANSFUSION: "Group match and prepare for exchange transfusion after seeing "
                                                    "TB/DB results",
    TreatmentType.CROSS_MATCH: "Cross-matched (1-2 hours for result)",

    TreatmentType.TSB_THEN_CONSULT: "Conduct TSB and consult with clinician",
    TreatmentType.TSB_2_HOURS: "Follow up on TSB values every 2 hours until > 2mg/dL below exchange threshold",
    TreatmentType.TCB_WITH_TIMING: "Follow up on TCB",
    TreatmentType.TSB_SHIELDED_TCB_BY_RISK: "Follow TSB/shielded TCB for 12-24 hours based on age and TCB/TSB "
                                            "trajectory",
    TreatmentType.TCSB_WITH_TIMING: "Follow up on TSB/TCB",

    TreatmentType.TO_EMERGENCY: "Admit to emergency neonatal units to apply phototherapy",

    TreatmentType.ON_PHOTO: "Put on phototherapy",
    TreatmentType.CONT_PHOTO: "Continue phototherapy",
    TreatmentType.DOUBLE_PHOTO: "Put on double phototherapy",
    TreatmentType.DOUBLE_PHOTO_STAT: "Put on double phototherapy STAT",
    TreatmentType.INCR_PHOTO_INTENSITY: "Consider increasing photo intensity",
    TreatmentType.OFF_PHOTO_WITH_TIMING: "Put off phototherapy and follow up",

    TreatmentType.PROVIDE_ELECTROLYTES: "Provide electrolytes if patient shows sign of dehydration",
    TreatmentType.NPO_AND_PERIPHERAL_IV: "Conduct NPO and provide IV",
    TreatmentType.NPO_CENTRAL: "Consult with a newborn fellow for considering doing a central line as they see fit",
    TreatmentType.IVIG: "Consider IVIG in infants with positive DAT",
    TreatmentType.EXCHANGE_TRANSFUSION: "Conduct exchange transfusion",
    TreatmentType.EXCHANGE_BY_BA_RATIO: "Consider exchange transfusion if A/B ratio is high",
}
