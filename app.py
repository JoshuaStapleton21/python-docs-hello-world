from flask import Flask, render_template, redirect, url_for, request
# Route for handling the login page logic
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')
