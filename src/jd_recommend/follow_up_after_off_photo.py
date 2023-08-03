from src.jd_models import Patient, AdmissionType
from datetime import timedelta


def has_risk_of_rebound(patient: Patient) -> bool:
    return patient.gestational_age < 38 or \
        patient.age_at_start_of_photo() < timedelta(hours=48) or \
        patient.has_hemolytic_diseases()


def handle_birth_admission(patient: Patient) -> str or list[str]:
    if has_risk_of_rebound(patient):
        return "6-12 hours after discontinuation and on the next day"
    else:
        return "On the next day after discontinuation"


# TODO: serve risk of rebound in a more elegant way
def handle_readmission(patient: Patient) -> str or list[str]:
    if patient.had_photo_during_birth_admission():
        return "The day after discontinuation while considering risk of rebound"
    else:
        return "1-2 days after discontinuation while considering risk of rebound"


def manage_follow_up_after_off_photo(patient: Patient):
    """
    Based on Figure 5: Follow up of TSB/TCB after photo discontinuation
    """
    match patient.admission_type:
        case AdmissionType.BIRTH_ADMISSION:
            return handle_birth_admission(patient)
        case AdmissionType.READMISSION:
            return handle_readmission(patient)
