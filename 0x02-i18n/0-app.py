#!/usr/bin/evn python3
"""
Flask App
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', methods=["GET"], strict_slashes=False)
def hello() -> str:
    """Hello route"""
    return render_template('0-index.html')


if __name__ = "__main__":
    app.run(host="0.0.0.0", port="5000")
