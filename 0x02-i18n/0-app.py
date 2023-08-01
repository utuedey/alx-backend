#!/usr/bin/env python3
"""
0-app module - A Basic flask app
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    """Home page of the app"""
    return render_template('templates/0-index.html')


if __name__ == "__main__":
    app.run()
