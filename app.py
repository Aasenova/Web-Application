from flask import Flask, render_template, request

app = Flask(__name__)  # name for the Flask app


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return f'{name} was a man who hated working. ' \
           f'He decided to rob a bank and escape to a tropical island. ' \
           f'He planned everything carefully and waited for the right moment. ' \
           f'He entered the bank with a mask and a gun and demanded all the money. ' \
           f'He stuffed the cash in his bag and ran out of the door. ' \
           f'He jumped into his car and drove away as fast as he could. ' \
           f'He was so happy that he started singing along to the radio. ' \
           f'He did not notice the police sirens behind him. ' \
           f'He also did not notice the sign that said “Road Closed”. ' \
           f'He crashed into a pile of bricks and was arrested.'

if __name__ == "__main__":
    app.run(debug=True)
