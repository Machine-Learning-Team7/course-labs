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

@app.route("/regressor")
def regressor():
        return render_template('regressor.html')

@app.route("/classifier")
def classifier():
        return render_template('classifier.html')

@app.route("/data")
def data():
        con=sqlite3.connect('./final_project/database/obesity.db')
        cur1=con.cursor();cur2=con.cursor()
        sample=raw.sample(5)
        # raw=cur1.execute("select * from rawData order by random() limit 5")
        clean=cur2.execute("select * from cleanedData order by random() limit 5")
        return render_template('data.html',raw=sample,clean=clean,varDesc=varDesc)

if __name__=="__main__":
        app.run(debug=True)

