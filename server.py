# By Andy Nguyen
# Registration Form

from flask import Flask, render_template, session, request, redirect, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisKeyIsSuperSecret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=['POST'])
def process():
    # Validation Rules
    session['flash_color'] = 'text-danger'
    if len(request.form['email']) < 1:
        flash("An email address must be provided.", 'email')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("The email provided is invalid. Please enter a valid email.", 'email')
    
    if len(request.form['first_name']) < 1:
        flash("First Name must be provided", 'first_name')
    elif len(request.form['first_name']) > 255:
        flash("Exceeded character limit", 'first_name')

    if len(request.form['last_name']) < 1:
        flash("Last Name must be provided", 'last_name')
    elif len(request.form['last_name']) > 255:
        flash("Exceeded character limit", 'last_name')

    if len(request.form['password']) < 1:
        flash("Password must be provided", 'password')
    elif len(request.form['password']) < 8:
        flash("Password must have 8 or more characters", 'password')
    elif len(request.form['password']) > 255:
        flash("Exceeded character limit", 'password')
    if request.form['password'].islower():
        flash("Password must contain at least 1 uppercase letter", 'password')
    if request.form['password'].isalpha():
        flash("Password must contain at least 1 number", 'password')
    elif request.form['password'] != request.form['confirm_password']:
        flash("Password and Password Confirmation should match", 'confirm_password')
    
    if '_flashes' in session:
        return redirect("/")
    else:
        session['flash_color'] = 'text-success'
        print(request.form)
        flash("Thanks for registering!", 'success')
        return redirect("/")


if __name__=="__main__":
    app.run(debug=True)