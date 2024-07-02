#!/usr/bin/env python3
"""
a simple flask application for renderng a templates
"""
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    """
    index view for renderting static html
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)