from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    
    return  render_template("index.html")


# @app.route("/classification")
# def dataset1():
#     return "Hello this is the Classifictaion Page"

# @app.route("/regression")
# def dataset2():
#     return "Hello this is the Regressiong Page"



if __name__ == "__main__":
    app.run()