from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# your code here

@app.route('/')
def home():
    return "hello world"

@app.route('/about-us')
def about_us():
    return "About Us"

# "magic code" -- boilerplate

if __name__ == '__main__':
    app.run(host=os.environ.get('IP')),
    port = int(os.environ.get('PORT')),
    debug = True
