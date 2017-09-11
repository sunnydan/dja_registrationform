from flask import Flask, render_template, redirect, request, flash, session
import re
import datetime
import time
app = Flask(__name__)
app.secret_key = "badonkadonk"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d$@$!%*?&]{8,}')


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=["POST"])
def process():
    valid = True
    if len(request.form['firstname']) < 1:
        flash("*First Name cannot be empty.")
        valid = False
    if len(request.form['lastname']) < 1:
        flash("*Last Name cannot be empty.")
        valid = False
    if not PASSWORD_REGEX.match(request.form['password']):
        flash("*Password must contain at least 1 capital letter and at least 1 number, and be at least 8 characters long.")
    if request.form['password'] != request.form['confirmpassword']:
        flash("*Password inputs must match.")
        valid = False
    if not EMAIL_REGEX.match(request.form['email']):
        flash("*Invalid Email Address.")
        valid = False
    print type(request.form['birthdate'])
    print request.form['birthdate']
    print time.strptime(request.form['birthdate'], "%Y-%m-%d")
    print type(time.localtime())
    print time.localtime()
    try:
        if time.strptime(request.form['birthdate'], "%Y-%m-%d") > time.localtime():
            flash("*Must select a Birthdate occuring in the past")
            valid = False
    except ValueError:
        flash("*Must select a valid Birthdate occuring in the past")
        valid = False
    if valid:
        return redirect('/result')
    else:
        return redirect('/')

@app.route("/result")
def result():
    return render_template('result.html')
    

app.run(debug=True)