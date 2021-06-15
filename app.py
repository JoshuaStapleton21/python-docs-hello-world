from flask import Flask, render_template, redirect, url_for, request
from flask.ext.assets import Bundle, Environment
from .. import app

bundles = {

    'home_js': Bundle(
        'js/bootsnav.js',
        'js/jquery.easypiechart.min.js',
        output='gen/home.js'),

    'home_css': Bundle(
        'css/animate.css',
        'css/bootsnav.css',
        'css/bootstrap.css',
        output='gen/home.css'),
}

assets = Environment(app)

assets.register(bundles)
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("home.html")
    