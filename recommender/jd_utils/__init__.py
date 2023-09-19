from pathlib import Path

HYPERBILIRUBINEMIA_RISKS: list[str] = [
    "GA < 38 weeks",
    "Jaundice within 24 hours",
    "Pre-discharge TCB close to PT",
    "Hemolysis or suspected",
    "Phototherapy before discharge",
    "History of parents or sibling requiring treatment",
    "Suboptimal breastfeeding",
    "Scalp hematoma or significant bruising",
    "Down syndrome",
    "Macrosomic infant of diabetic mother"
]

NEUROTOXICITY_RISKS: list[str] = [
    "ABO or Rh incompatibility",
    "Other hemolytic diseases",
    "GA < 38 weeks",
    "Albumin < 3g/dL",
    "Sepsis",
    "Clinically unstable in past 24 hours"
]

PROJECT_ROOT: Path = Path(__file__).parent.parent.parent
