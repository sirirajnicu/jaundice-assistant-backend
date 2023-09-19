from recommender.jd_models import Patient, PhototherapyType, Gender
from follow_up_after_off_photo import manage_follow_up_after_off_photo


def tsb_lt_threshold_with_photo(patient: Patient,
                                photo_threshold: float) -> str or list[str]:
    """
    Based on Figure 3 - left arm
    """
    tsb_diff = photo_threshold - patient.tsb_value[-1].data

    if tsb_diff < 2.0:
        return [
            "Continue phototherapy",
            "Follow TSB/shielded TCB in 12-24 hours based on age," +
            "neurotoxic risk, TSB and TCB trajectory"
        ]
    elif patient.photo_therapy_record[-1].data == PhototherapyType.SINGLE:
        return "Off photo and follow-up"
    else:
        return [
            "On single phototherapy and follow TSB/shielded TCB in 12-24" +
            "hours based on age, neurotoxic risk, TCB and TSB trajectory",
            "Off photo and follow-up"
        ]


def tsb_lt_threshold_no_photo(patient: Patient) -> str or list[str]:
    """
    Based on Figure 3 - right arm
    """
    if patient.is_within_96hrs_after_phototherapy():
        return "Follow up on TSB/TCB " + manage_follow_up_after_off_photo(patient)

    elif (patient.change_rate_first_day() > 0.3 or
          patient.change_rate_after_first_day() > 0.2 or
          patient.had_jaundice_within_first_24hrs()):
        treatments = [
            "TSB + consult clinician",
            "CBC, blood smear, reti count",
            "Blood group, DAT",
        ]
        if patient.gender == Gender.MALE:
            treatments.append("G6PD")
        return treatments

    else:
        return "TSB/TCB follow-up"


def manage_tsb_under_threshold(patient: Patient,
                               photo_threshold: float) -> str or list[str]:
    """
    Based on Figure 3: Management of TSB levels that are below phototherapy threshold
    """
    if patient.is_between_photo_therapy():
        return tsb_lt_threshold_no_photo(patient)
    else:
        return tsb_lt_threshold_with_photo(patient, photo_threshold)
