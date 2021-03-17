from flask import Flask, render_template
from app import app



@app.route('/')

def aws():
	return render_template('home.html')

@app.route('/portfolio')

def portfolio():

    return render_template('portafolio.html')

@app.route('/aws')

def home():
    return render_template('aws.html')

@app.route('/home/slides')

def slides():
	return render_template("slides.html")




