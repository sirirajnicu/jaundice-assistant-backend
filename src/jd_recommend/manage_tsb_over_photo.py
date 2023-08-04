from src.jd_models import Patient, PhototherapyType


def handle_far_below_threshold(patient: Patient) -> str or list[str]:
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


def handle_close_below_threshold(patient: Patient) -> str or list[str]:
    pass


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
