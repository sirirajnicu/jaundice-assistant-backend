from src.jd_models import Patient, PhototherapyType


def handle_far_below_threshold(patient: Patient) -> str or list[str]:
    """
    Based on Figure 4 - left arm
    """
    treatments = [
        "Follow TSB/shielded TCB for 12-24 hours based on age and TCB/TSB trajectory",
        "PE and work for causes"
    ]
    match patient.on_photo_therapy:
        case PhototherapyType.NONE:
            treatments.append("Put on photo")
        case PhototherapyType.SINGLE:
            treatments.append("Consider switching to double photo")
        case PhototherapyType.DOUBLE:
            treatments.append("Increase photo efficiency")

    return treatments


# TODO: make a pop-up on user screen when this is called
def request_bind_score() -> float:
    return 0.0


def handle_close_below_threshold(patient: Patient) -> str or list[str]:
    """
    Based on Figure 4 - middle arm
    """
    treatments = []
    match patient.on_photo_therapy:
        case PhototherapyType.NONE:
            treatments.append("Put on double photo STAT")
        case PhototherapyType.SINGLE:
            treatments.append("Consider switching to double photo")
        case PhototherapyType.DOUBLE:
            treatments.append("Consider increasing photo intensity")

    if request_bind_score() >= 4:
        treatments.append("Do an exchange transfusion")
    else:
        treatments.extend([
            "Continue phototherapy",
            "Consider exchange transfusion if A/B ratio is high",
            "NPO, peripheral IV",
            "Cross-matched (1-2 hours of waiting time)",
            "PE and work up for cause",
            "Follow up on TSB values every 2 hours until > 2mg/dL below exchange threshold",
            "Consider IVIG in infants with DAT positive"
        ])


def manage_tsb_over_threshold(patient: Patient, exchange_threshold: float) -> str or list[str]:
    """
    Based on Figure 4: Managements of TSB levels that are exceeding phototherapy threshold
    """
    if patient.tsb_value[-1] >= exchange_threshold:
        return [
            "Put on double phototherapy STAT and exchange transfusion",
            "NPO, central line while on photo",
            "Cross-matched (1-2 hours of waiting time)",
            "PE and work up for cause",
            "Follow up on TSB values every 2 hours until > 2mg/dL below exchange threshold",
        ]

    tsb_diff = exchange_threshold - patient.tsb_value[-1]
    if tsb_diff > 2.0:
        return handle_far_below_threshold(patient)
    else:
        return handle_close_below_threshold(patient)
