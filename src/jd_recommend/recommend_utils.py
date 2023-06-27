from src.jd_models import Patient, PhototherapyType


def tcb_within_lt3_geq15_from_threshold(tcb_value: float,
                                        photo_threshold: float) -> bool:
    threshold_diff = photo_threshold - tcb_value
    return threshold_diff <= 3.0 or tcb_value >= 15.0


def compute_first_day_tcb(patient: Patient) -> float:
    # higher TCB => bad, if tcb >= 15 then tsb
    # rate rising instead of latest within first thrs and REQUIRE at least 2 data points
    # take latest only
    # difference between same kind only
    return 0.0


def compute_later_tcb(patient: Patient) -> float:
    # same as before
    # if cross over between first day and after => if last data point within 24 then just use it
    return 0.0


def jx_within_first_24(patient: Patient) -> bool:
    if patient.tcb_value is None or patient.tsb_value is None:
        return False
    # check TCB and TSB and see if > 2 mg/dL
    # if no data, return False
    return False


def is_within_96hrs_after_phototherapy(patient: Patient) -> bool:
    # need to keep track of when patient is on photo
    # on photo: need to keep track of when patient is on and off photo and compute no. hrs from there
    # 96 hrs is right after going off photo
    return False


def patient_between_phototherapy(patient: Patient) -> bool:
    # if turned on and not off yet => True
    return patient.on_photo_therapy == PhototherapyType.NONE
