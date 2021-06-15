from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("home.html")
    