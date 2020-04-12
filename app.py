from flask import Flask, redirect, url_for, render_template
from flask_restful import Api
from resources.todo import Aapi
app = Flask(__name__)
api = Api(app)

@app.route("/")
def home():
    return render_template("htmlss.html", content="Testing", x=4)
@app.route("/api")
def apihome():
    return render_template("htmlss.html")
@app.route("/api/")
def apihomered():
    return render_template("htmlss.html")
if __name__ == "__main__":
  app.run(debug=True)