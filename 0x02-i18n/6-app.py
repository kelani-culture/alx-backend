from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext

app = Flask(__name__)


class Config:
    LANGUAGES = ["en", "fr", "kg"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)



users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user(login_as: int = None):
    return users.get(int(login_as)) if login_as else None


@app.before_request
def before_request():
    req = request.args.get('login_as')
    user = get_user(req)
    g.user = user

@babel.localeselector
def get_locale():
    lang = request.args.get('lang') or g.user.get('locale')
    if lang:
        return lang
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index():
    """
    index view for renderting static html
    """
    user = g.user
    return render_template("6-index.html", user=user)


if __name__ == '__main__':
    app.run(debug=True)