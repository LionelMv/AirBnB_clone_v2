#!/usr/bin/python3
"""
This scripts starts a Flask web app.
The web app must be listening on 0.0.0.0:5000
"""

from flask import Flask, render_template

app = Flask(__name__, template_folder='../templates')


@app.route("/", strict_slashes=False)
def hello():
    """diplays Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """diplays HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_display(text):
    """Displaying a variable"""
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def py_display(text='is_cool'):
    """python is fun"""
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def num_display(n):
    """function displays integer only"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def template_num(n):
    "renders template to diplay integer only"
    return render_template("5-number.html", num=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
