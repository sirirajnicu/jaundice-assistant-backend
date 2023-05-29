from jd_models import Patient, PhototherapyType


def patient_between_phototherapy(patient: Patient) -> bool:
    return patient.on_photo_therapy == PhototherapyType.NONE


def tsb_lt_threshold_no_photo(patient: Patient,
                              photo_threshold: float) -> str or list[str]:
    tsb_diff = photo_threshold - patient.tsb_value[-1]
    if tsb_diff < 0:
        return "No treatment"
    elif tsb_diff < 2.0:
        return [
            "Continue phototherapy",
            "Follow TSB/shielded TCB in 12-24 hours based on age," +
            "neurotoxic risk, TSB and TCB trajectory"
        ]
    elif patient.on_photo_therapy == PhototherapyType.SINGLE:
        return "Off photo and follow-up"
    else:
        return [
            "On single phototherapy and follow TSB/shielded TCB in 12-24" +
            "hours based on age, neurotoxic risk, TCB and TSB trajectory",
            "Off photo and follow-up"
        ]


def tsb_lt_threshold_with_photo(patient: Patient,
                                photo_threshold: float) -> str or list[str]:
    return ""


def tsb_under_threshold(patient: Patient,
                        photo_threshold: float) -> str or list[str]:
    if patient_between_phototherapy(patient):
        return tsb_lt_threshold_no_photo(patient, photo_threshold)
