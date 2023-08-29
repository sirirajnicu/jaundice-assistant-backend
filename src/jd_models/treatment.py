from aenum import Enum
from datetime import timedelta
from typing import Dict, List

TreatmentType = Enum("TreatmentType", " ".join([
    # the treatment type names/acronyms go here
]))

MSG_DB: Dict[TreatmentType, List[str]] = {
    # stores the base msg for each treatment type
}

assert len(TreatmentType) == len(MSG_DB)


class Treatment:
    type: TreatmentType
    follow_up_timing: timedelta

    def get_treatment_msg(self) -> str:
        return ...

    def update_follow_up_time(self, new_timing: timedelta):
        self.follow_up_timing = new_timing
