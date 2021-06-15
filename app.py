from flask import Flask, render_template, redirect, url_for, request
from flask.ext.assets import Bundle, Environment
from .. import app

# bundles = {

#     'home_js': Bundle(
#         'js/lib/jquery-1.10.2.js',
#         'js/home.js',
#         output='gen/home.js'),

#     'home_css': Bundle(
#         'css/lib/reset.css',
#         'css/common.css',
#         'css/home.css',
#         output='gen/home.css'),

#     'admin_js': Bundle(
#         'js/lib/jquery-1.10.2.js',
#         'js/lib/Chart.js',
#         'js/admin.js',
#         output='gen/admin.js'),

#     'admin_css': Bundle(
#         'css/lib/reset.css',
#         'css/common.css',
#         'css/admin.css',
#         output='gen/admin.css')
# }

# assets = Environment(app)

# assets.register(bundles)
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("home.html")
    