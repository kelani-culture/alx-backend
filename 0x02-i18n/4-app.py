from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    lang = request.args.get('lang') or None
    if lang:
        return lang
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index():
    """
    index view for renderting static html
    """
    return render_template("4-index.html")

