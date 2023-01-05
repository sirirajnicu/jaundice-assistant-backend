from flask import Flask
from src.routes.routes import routes

app = Flask(__name__)
app.register_blueprint(routes)


def dev():
    app.run(debug=True, use_reloader=False)
