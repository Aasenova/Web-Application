from flask import Flask, render_template, request

app = Flask(__name__) #Turn this file into Flask application

@app.route('/') #Here is the code which I want the server to execute, when user visit website
def home():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return render_template('home.html', name=name)

@app.route('/index', methods=['POST'])
def index():
    message = request.form['message']
    return render_template('home.html', message=message)
