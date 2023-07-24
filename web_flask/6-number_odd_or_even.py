#!/usr/bin/python3
"""
This scripts starts a Flask web app.
The web app must be listening on 0.0.0.0:5000
"""

from flask import Flask, render_template

app = Flask(__name__)
# app = Flask(__name__, template_folder="../templates")
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """diplays Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """diplays HBNB"""
    return "HBNB"


@app.route("/c/<text>")
def c_display(text):
    """Displays custom text given"""
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route("/python/")
@app.route("/python/<text>")
def py_display(text='is_cool'):
    """Displays custom text given"""
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route("/number/<int:n>")
def text_if_int(n):
    """Displays text if integer is given."""
    return f"{n} is a number"


@app.route("/number_template/<int:n>")
def html_if_int(n):
    "Displays html page only if int is given"
    return render_template("5-number.html", num=n)


@app.route("/number_odd_or_even/<int:n>")
def num_odd_even(n):
    "Displays html page only if int is given"
    # another way of implementing it.
    # odd_or_even = "even" if (n % 2 == 0) else "odd"
    # return render_template('6-number_odd_or_even.html',
    #                       n=n, odd_or_even=odd_or_even)
    return render_template("6-number_odd_or_even.html", num=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
