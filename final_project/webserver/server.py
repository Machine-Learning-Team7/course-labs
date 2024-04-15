from flask import Flask, render_template, request, url_for
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



@app.route("/")
def welcome():
        return render_template('welcome.html')

@app.route("/about")
def about():
        return render_template('about.html')

@app.route("/regressor", methods=["GET", "POST"])
def regressor():
        if request.method == "POST":
                age=request.form["age"], height=request.form['height'], weight=request.form['weight'], fcvc=request.form['fcvc'], ncp=request.form['ncp'], ch20=request.form['ch20'], faf=request.form['faf'], tue=request.form['tue']
                return redirect(url_for("reg_answers", newAge=age, newHeight=height, newWeight=weight, newFcvc=fcvc, newNcp=ncp, newCh20=ch20, newFaf=faf, newTue=tue))
        else: 
                return render_template('regressor.html')


@app.route("/<newAge>, <newHeight>, <newWeight>, <newFcvc>, <newNcp>, <newCh20>, <newFaf>, <newTue>")
def reg_answers(newAge, newHeight, newWeight, newFcvc, newNcp, newCh20, newFaf, newTue):
        return render_template('reg_answers.html')

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

