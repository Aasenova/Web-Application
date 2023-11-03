from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return"Welcome to my Flask web app"