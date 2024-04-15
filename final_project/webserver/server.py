from flask import Flask, render_template, request, url_for, session
import sqlite3
from pathlib import Path
import pandas as pd
from ucimlrepo import fetch_ucirepo
import pandas as pd
raw=pd.DataFrame
obesity = fetch_ucirepo(id=544)
features=obesity.data.features
target=obesity.data.targets
raw=pd.concat([features,target],axis=1)
varDesc=obesity.variables

app=Flask(__name__)
app.secret_key="group project 7"


@app.route("/")
def welcome():
        return render_template('welcome.html')

@app.route("/about")
def about():
        return render_template('about.html')

@app.route("/regressor", methods=["GET", "POST"])
def regressor():
        if request.method == "POST":
                reg_answers = age=request.form["age"], height=request.form['height'], weight=request.form['weight'], fcvc=request.form['fcvc'], ncp=request.form['ncp'], ch20=request.form['ch20'], faf=request.form['faf'], tue=request.form['tue']
                session["reg_answers"] = reg_answers
                return redirect(url_for("reg_answers"))
        else: 
                return render_template('regressor.html')


@app.route("/reg_answers")
def reg_answers():
        if "reg_answers" in session:
                reg_answers = session["reg_answers"]
                return f"<h2>newAge, newHeight, newWeight, newFcvc, newNcp, newCh20, newFaf, newTue</h2>"
        else:
                return redirect(url_for("regressor"))

@app.route("/classifier")
def classifier():
        return render_template('classifier.html')

@app.route("/data/<model>")
def data(model):
        if(model=='regression'):
                con=sqlite3.connect('./final_project/database/obesity.db')
                cur1=con.cursor();cur2=con.cursor()
                sample=raw.sample(5)
                # raw=cur1.execute("select * from rawData order by random() limit 5")
                clean=cur2.execute("select * from cleanedData order by random() limit 5")
                return render_template('data_reg.html',raw=sample,clean=clean,varDesc=varDesc)
        if(model=='classification'):
                con=sqlite3.connect('./final_project/database/obesity.db')
                cur1=con.cursor();cur2=con.cursor()
                sample=raw.sample(5)
                # raw=cur1.execute("select * from rawData order by random() limit 5")
                clean=cur2.execute("select * from cleanedData order by random() limit 5")
                return render_template('data_class.html',raw=sample,clean=clean,varDesc=varDesc)

if __name__=="__main__":
        app.run(debug=True)

