from flask import Flask, render_template,request
import pickle
import joblib
from sqlite3 import *
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check" ,methods=["POST"])
def check():
    r2 = request.form["r2"]
    if r2 == "NO":
        YF=1
    else:
        YF=2
    r3 = request.form["r3"]
    if r3 == "NO":
        AN=1
    else:
        AN=2
    r4 = request.form["r4"]
    if r4 == "NO":
        PP=1
    else:
        PP=2
    r5 = request.form["r5"]
    if r5 == "NO":
        CD=1
    else:
        CD=2
    r6 = request.form["r6"]
    if r6 == "NO":
        FA=1
    else:
        FA=2     
    r7 = request.form["r7"]
    if r7 == "NO":
        AL=1
    else:
        AL=2  
    r8 = request.form["r8"]
    if r8 == "NO":
        WH=1
    else:
        WH=2  
    r9 = request.form["r9"]
    if r9 == "NO":
        AC=1
    else:
        AC=2  
    r10 = request.form["r10"]
    if r10 == "NO":
        CO=1
    else:
        CO=2   
    r12 = request.form["r12"]
    if r12 == "NO":
        SD=1
    else:
        SD=2     
    r13 = request.form["r13"]
    if r13 == "NO":
        CP=1
    else:
        CP=2   
    d=[[YF,AN,PP,CD,FA,AL,WH,AC,CO,SD,CP]]
    with open("./lung cancer.model","rb") as f:
        model=joblib.load(f)
    ans=model.predict(d)
    ans1=ans[0]
    if (ans1 == 0):
      res="NO"
    else:
      res="YES"
    return render_template("index.html",msg=res)

if __name__ == "__main__":
    app.run(debug=True)