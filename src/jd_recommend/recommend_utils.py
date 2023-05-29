from jd_models import Patient, PhototherapyType


def tcb_within_lt3_geq15_from_threshold(tcb_value: float,
                                        photo_threshold: float) -> bool:
    threshold_diff = photo_threshold - tcb_value
    return threshold_diff <= 3.0 or tcb_value >= 15.0


def compute_first_day_tcb(patient: Patient) -> float:
    return 0.0


def compute_later_tcb(patient: Patient) -> float:
    return 0.0


def jx_within_first_24(patient: Patient) -> bool:
    return False


def is_within_96hrs_after_phototherapy(patient: Patient) -> bool:
    return False


def patient_between_phototherapy(patient: Patient) -> bool:
    return patient.on_photo_therapy == PhototherapyType.NONE
