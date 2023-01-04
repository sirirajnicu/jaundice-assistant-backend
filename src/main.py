from flask import Flask, render_template
from .routes.routes import routes

app = Flask(__name__)
app.register_blueprint(routes)


def run():
    app.run(debug=True, use_reloader=False)
