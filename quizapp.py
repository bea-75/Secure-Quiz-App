#to set secret key
#C:\Users\P3\Desktop\folder python is in>set SECRET_KEY=key you want

import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

app.secret_key=os.environ["SECRET_KEY"];

q = "renderM1"
    
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/math")
def renderMath():
    return render_template("math-start.html")
    
@app.route("/math-tst-q1", methods=['GET','POST'])
def renderM1():
    global q
    
    if "q1" in session: 
        return redirect(url_for(q))
    else:
        q = "renderM1"
        return render_template("m1.html")

@app.route("/math-tst-q2", methods=['GET','POST'])
def renderM2():
    global q
    
    if 'q1' not in session:
        session["q1"]=request.form["q1"]
    
    if "q2" in session:
        return redirect(url_for(q))
    else:
        q = "renderM2"
        return render_template("m2.html")
    
@app.route("/math-tst-q3", methods=['GET','POST'])
def renderM3():
    global q
    
    if 'q2' not in session:
        session["q2"]=request.form["q2"]
    
    if "q3" in session:
        return redirect(url_for(q))
    else:
        q = "renderM3"      
        return render_template("m3.html")

    
@app.route("/math-tst-q4", methods=['GET','POST'])
def renderM4():
    global q
    
    if 'q3' not in session:
        session["q3"]=request.form["q3"]    
    
    if "q4" in session:
        return redirect(url_for(q))
    else:
        q = "renderM4"
        return render_template("m4.html")
    
@app.route("/math-tst-q5", methods=['GET','POST'])
def renderM5():
    global q
    
    if 'q4' not in session:
        session["q4"]=request.form["q4"]
    
    if "q5" in session:
        return redirect(url_for(q))
    else:
        q = "renderM5"
        return render_template("m5.html")

@app.route("/math-tst-end", methods=['GET','POST'])
def renderMathEnd():
    global q
    
    q = "renderMathEnd"
    if 'q5' not in session:
        session["q5"]=request.form["q5"]
    return render_template("math-end.html")
    
@app.route("/start-over")
def renderStartOver():
    q = "renderMath"
    session.clear()
    return redirect("/")
    
if __name__=="__main__":
    app.run(debug=True)