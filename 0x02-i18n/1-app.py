from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

app.route('/')
def index():
    """
    index view for renderting static html
    """
    return render_template('0-index.html')

