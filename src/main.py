from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("main.html")


@app.route("/current-patient/")
def current_patient():
    return render_template("views/current-patient.html")


@app.route("/consultation-status/")
def consultation_status():
    return render_template("views/consultation-status.html")


@app.route("/order-review/")
def order_review():
    return render_template("views/order-review.html")


@app.route("/case-review/")
def case_review():
    return render_template("views/case-review.html")


def run():
    app.run(debug=True, use_reloader=False)
