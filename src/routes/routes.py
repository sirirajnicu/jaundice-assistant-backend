from flask import Blueprint, render_template

from src.jd_utils import split_risks
from src.jd_utils.const import HYPERBILIRUBINEMIA_RISKS, NEUROTOXICITY_RISKS

routes = Blueprint("routes", __name__)


@routes.route("/")
def main():
    return render_template("main.html")


@routes.route("/current-patient/")
def current_patient():
    hyper_risks: list[list[str]] = split_risks(HYPERBILIRUBINEMIA_RISKS)
    neuro_risks: list[list[str]] = split_risks(NEUROTOXICITY_RISKS)
    return render_template("views/current-patient.html", risks1=hyper_risks, risks2=neuro_risks,
                           is_risky1=True, is_risky2=False)


@routes.route("/consultation-status/")
def consultation_status():
    return render_template("views/consultation-status.html")


@routes.route("/order-review/")
def order_review():
    return render_template("views/order-review.html")


@routes.route("/case-review/")
def case_review():
    return render_template("views/case-review.html")
