#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 21:07:41 2019

@author: nikhildikshit
"""
import test
import flask
# from flask_restful import Resource, Api

app = flask.Flask(__name__, template_folder='templates')
@app.route('/', methods=['GET', 'POST'])

def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    if flask.request.method == 'POST':
        income = flask.request.form['income']
        credit = flask.request.form['credit']
        IncRat = flask.request.form['IncRat']
        ltv = flask.request.form['ltv']
        loan_amount = flask.request.form['loan_amount']
        # state = flask.request.form['State']
        # year = flask.request.form['Year']  
        return flask.render_template('main.html',
                                    result = test.testPred(income, credit, IncRat, ltv, loan_amount))
if __name__== "__main__":
    app.run(debug=True)


