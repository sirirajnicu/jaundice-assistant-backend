from flask import Blueprint, redirect, url_for

routes = Blueprint("routes", __name__)


@routes.route("/")
def main():
    return redirect(url_for('routes.current_patient'))


@routes.route("/current-patient/")
def current_patient():
    pass


@routes.route("/consultation-status/")
def consultation_status():
    pass


@routes.route("/order-review/")
def order_review():
    pass


@routes.route("/case-review/")
def case_review():
    pass
