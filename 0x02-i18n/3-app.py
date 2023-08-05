#!/usr/bin/env python3
"""
A Basic flask app
"""
from flask import request
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """babel class configuration"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Retrieves the locale for a webpage"""
    return request.accept_languages.best_match(
        app.config["LANGUAGES"])


@app.route("/")
def index():
    """app home page"""
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run()
