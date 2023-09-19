from recommender.jd_utils.__init__ import PROJECT_ROOT
from recommender.jd_models import Patient, NeurotoxicityRisk, Threshold
from pathlib import Path
from datetime import datetime, timedelta
import pandas as pd
from math import floor

RESOURCES_ROOT = PROJECT_ROOT.joinpath("./resources")

PHOTO_NO_RISK = "./photo_no_risk/"
PHOTO_AT_RISK = "./photo_at_risk/"

EXCHANGE_NO_RISK = "./exchange_no_risk/"
EXCHANGE_AT_RISK = "./exchange_at_risk/"

HOL_INDEX_NAME = "HOL"
TSB_INDEX_NAME = "TSB"


def seconds_to_hours(time_dif: timedelta) -> int:
    secs_flt = time_dif.total_seconds() // timedelta(days=1).total_seconds()
    secs_int = floor(secs_flt)
    return max(secs_int, 1)


def get_ga_as_filename(patient: Patient) -> str:
    return f"./GA{patient.gestational_age}.csv"


def get_threshold_path_from_ga(patient: Patient,
                               threshold_type: Threshold) -> Path:
    match (threshold_type, patient.neuro_risk):
        case (Threshold.PHOTO, NeurotoxicityRisk.NO_RISK):
            return RESOURCES_ROOT.joinpath(PHOTO_NO_RISK).joinpath(get_ga_as_filename(patient))
        case (Threshold.PHOTO, NeurotoxicityRisk.AT_RISK):
            return RESOURCES_ROOT.joinpath(PHOTO_AT_RISK).joinpath(get_ga_as_filename(patient))
        case (Threshold.EXCHANGE, NeurotoxicityRisk.NO_RISK):
            return RESOURCES_ROOT.joinpath(EXCHANGE_NO_RISK).joinpath(get_ga_as_filename(patient))
        case (Threshold.EXCHANGE, NeurotoxicityRisk.AT_RISK):
            return RESOURCES_ROOT.joinpath(EXCHANGE_AT_RISK).joinpath(get_ga_as_filename(patient))


def compute_photo_threshold(patient: Patient) -> float:
    """ From appendix 2 and 3 """
    threshold_file = get_threshold_path_from_ga(patient, Threshold.PHOTO)
    threshold_data = pd.read_csv(threshold_file).set_index(HOL_INDEX_NAME)

    birth_til_now: timedelta = datetime.now() - patient.birth_date_time
    hours_of_life = seconds_to_hours(birth_til_now)

    return threshold_data.loc[hours_of_life, TSB_INDEX_NAME]


def compute_exchange_threshold(patient: Patient) -> float:
    """ From appendix 4 and 5 """
    threshold_file = get_threshold_path_from_ga(patient, Threshold.EXCHANGE)
    threshold_data = pd.read_csv(threshold_file).set_index(HOL_INDEX_NAME)

    birth_til_now: timedelta = datetime.now() - patient.birth_date_time
    hours_of_life = seconds_to_hours(birth_til_now)

    return threshold_data.loc[hours_of_life, TSB_INDEX_NAME]


if __name__ == "__main__":
    print(compute_photo_threshold(Patient.default()))
    print(compute_exchange_threshold(Patient.default()))
