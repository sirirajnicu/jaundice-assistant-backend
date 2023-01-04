from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("main.html")


def run():
    app.run(debug=True, use_reloader=False)
