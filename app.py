from flask import Flask, render_template, Response, request, redirect
import numpy as np

app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/dataanalysis')
def dataanalysis():
    return render_template('dataanalysis.html')


if __name__=="__main__":
    app.run(debug=True)