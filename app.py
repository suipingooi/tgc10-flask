from flask import Flask, render_template, request, redirect, url_for
import os
import random

app = Flask(__name__)

# your code here


@app.route('/')
def home():
    return render_template('home.template.html')


@app.route('/about-us')
def about_us():
    return "<h1>About Us</h1>"

@app.route('/our-history')
def our_history():
    return render_template('history.template.html')

@app.route('/lucky')
def lucky_number():
    number = random.randint(1000, 9999)
    return "<h1>Your lucky number is </h1>" + str(number)


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host='localhost',
            port=8080,
            debug=True)
