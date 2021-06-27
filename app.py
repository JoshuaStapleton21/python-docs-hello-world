# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('creative_designers.html')

# @app.route('/about/')
# def about():
#     return render_template('about.html')
    
# if __name__ == '__main__':
# 	app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/hello.html')
def hello():
    return render_template('hello.html')

@app.route('/hoi.html')
def skee():
    return render_template('templates/2020/10/24/hoi.html')
    
if __name__ == '__main__':
	app.run(debug=True)