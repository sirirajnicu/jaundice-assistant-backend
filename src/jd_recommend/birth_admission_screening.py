from jd_models import Patient, Gender


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


def handle_tcb_lt_photo_threshold(patient: Patient,
                                  photo_threshold: float) -> str or list[str]:
    if tcb_within_lt3_geq15_from_threshold(patient.tcb_value, photo_threshold):
        return "Conduct TSB and consult Clinician"

    elif (compute_first_day_tcb(patient) > 0.3 or
            compute_later_tcb(patient) > 0.2 or
            jx_within_first_24(patient)):
        treatments = [
            "TSB + consult clinician",
            "CBC, blood smear, reti count",
            "Blood group, DAT",
        ]
        if patient.gender == Gender.MALE:
            treatments.append("G6PD")
        return treatments

    else:
        return "Follow up with TCB"


def handle_tcb_geq_photo_threshold(patient: Patient,
                                   blood_threshold: float) -> str or list[str]:
    diff_from_threshold = patient.tcb_value - blood_threshold

    if diff_from_threshold < -2.0:
        treatments = [
            "TSB + consult clinician",
            "CBC, blood smear, reti count",
            "Blood group, DAT",
        ]
        if patient.gender == Gender.MALE:
            treatments.append("G6PD")
        return treatments

    else:
        treatments = [
            "Admit to emergency neonatal units",
            "Double phototherapy",
            "TB/DB, albumin, CBC, blood smea, reti count",
            "Blood group, DAT",
            "Group match",
        ]
        if patient.gender == Gender.MALE:
            treatments.append("G6PD")
        return treatments


# TODO: change return type to a treatment class
def recommend_from_tcb(patient: Patient,
                       photo_threshold: float,
                       blood_threshold: float) -> str or list[str]:
    if patient is None or len(patient.tcb_value) <= 0:
        raise ValueError("Invalid Patient object")

    if patient.tcb_value[-1] < photo_threshold:
        return handle_tcb_lt_photo_threshold(patient, photo_threshold)
    else:
        return handle_tcb_geq_photo_threshold(patient, blood_threshold)
