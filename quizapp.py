#to set secret key
#C:\Users\P3\Desktop\folder python is in>set SECRET_KEY=key you want

import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

app.secret_key=os.environ["SECRET_KEY"];

@app.route("/")
def renderHome():
    return render_template("home.html")
    
@app.route("/math-test")
def renderMath():
    return render_template("math-tst.html")