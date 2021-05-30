from flask import Flask, jsonify, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import csv
import numpy as np
import pandas as pd

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret_key'

class infoForm(FlaskForm):
    prn = StringField("Enter PR number of product: ")
    submit = SubmitField('Submit')

dataframe1 = pd.read_csv("static/data/Book1csvMAC.csv")

def datafunc(dataframe1,prn):
    prn = int(prn)
    prn_dataframe = dataframe1[dataframe1['PR number'] == prn]
    vendors_involved = prn_dataframe['vendor name'].unique()
    return vendors_involved

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/adminpanel')
def adminpanel():
    return render_template('adminpanel.html')

@app.route('/empsignin')
def empsignin():
    return render_template('empsignin.html')

@app.route('/vendorsignin')
def vendorsignin():
    return render_template('vendorsignin.html')

@app.route('/empassist', methods=['GET', 'POST'])
def empassist():
    prn = False
    form = infoForm()
    vendors_involved = []

    if form.validate_on_submit():
        vendors_involved = []
        prn = form.prn.data
        vendors_involved = datafunc(dataframe1,prn)
        form.prn.data = ''
    
    return render_template('empassist.html', form = form, prn = prn, vendors_involved = vendors_involved)

@app.route('/vendorassist')
def vendorassist():
    return render_template('vendorassist.html')

if __name__ == "__main__":
    app.run(debug=True)
