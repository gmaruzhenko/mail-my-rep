from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)
import spamMyReps


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submitted',methods = ['POST', 'GET'])
def send():
    if request.method == 'POST':
        name = request.form['name']
        subject  = request.form['subject']
        address  = request.form['address']
        message  = request.form['message']

        spamMyReps.main(name, address, subject, message)

        return render_template('submitted.html')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()
