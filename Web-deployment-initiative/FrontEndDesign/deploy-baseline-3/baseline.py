#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 18:42:32 2019

@author: nikhildikshit
"""

import pandas as pd

df = pd.read_csv('/Users/sadidasiddiqui/Desktop/untitledfolder/Baseline_Dataframe.csv')

def calculate(income, credit, IncRat, loan_amount, ltv, year, state):
    def createBaseLine(year):
        # Year comes in the 
        b_year = df[df["Year"] == year]
        b_year_temp = b_year.groupby("StateName").agg(lambda x: x.value_counts().index[0])
        byear = b_year_temp[["Income" , "IncRat", "Amount"]]
        byear["Rate"] = b_year["Rate"].groupby(df["StateName"]).mean()
        byear["LTV"] = b_year["LTV"].groupby(df["StateName"]).mean()
        byear["GDP"] = b_year["GDP"].groupby(df["StateName"]).mean()
        byear["Unemployment"] = b_year["Unemployment"].groupby(df["StateName"]).mean()
        byear["Real State Growth %"] = b_year["Real State Growth %"].groupby(df["StateName"]).mean()
        return byear
    
    baseline_2010 =  createBaseLine(2010)
    baseline_2011 =  createBaseLine(2011)
    baseline_2012 =  createBaseLine(2012)
    baseline_2013 =  createBaseLine(2013)
    baseline_2014 =  createBaseLine(2014)
    baseline_2015 =  createBaseLine(2015)
    baseline_2016 =  createBaseLine(2016)
    baseline_2017 =  createBaseLine(2017)
        
    # Baseline Model Definition
    def scoreIncome(income, baseline_income):
        if income >= baseline_income:
            return 10
        else:
            return 5
    
    def scoreCredit(credit):
        if credit >= 4:
            return 10
        else:
            return 5
    
    def scoreIncRatio(IncRat, baseline_IncRat):
        if IncRat > baseline_IncRat:
            return 10
        else:
            return 5
    
    def scoreLoanAmount(loan_amount, baseline_loan_amount):
        if loan_amount < baseline_loan_amount+5000.0:
            return 10
        else:
            return 5
    
    def scoreLTV(ltv, baseline_ltv):
        if income > baseline_income:
            return 10
        else:
            return 5
    
    def cartModel(baseline_income,baseline_IncRat, baseline_loan_amount, baseline_ltv, income, credit, IncRat,loan_amount, ltv):
        profile_score = 0 
        profile_score += scoreIncome(income, baseline_income)
        profile_score += scoreCredit(credit)
        profile_score += scoreIncRatio(IncRat, baseline_IncRat)
        profile_score += scoreLoanAmount(loan_amount, baseline_loan_amount)
        profile_score += scoreLTV(ltv, baseline_ltv)
        return profile_score
    
    """
    def evaluatorApplication(profile_score):
        if profile_score >= 30:
            print("\nStatus: Approved")
        else:
            print("\nStatus: Declined")
            """
    
    # state = "New York"
    # Feeding the above value into baseline Model
    baseline_dict = {
                     2010: baseline_2010,\
                     2011: baseline_2011,\
                     2012: baseline_2012,\
                     2013: baseline_2013,\
                     2014: baseline_2014,\
                     2015: baseline_2015,\
                     2016: baseline_2016,\
                     2017: baseline_2017
                    }
    
    baseline_df = baseline_dict[year]
    baseline_df.loc[state]
    baseline_income       = float(baseline_df.loc[state][0])
    baseline_IncRat       = float(baseline_df.loc[state][1])
    baseline_loan_amount  = float(baseline_df.loc[state][2])
    baseline_ltv          = float(baseline_df.loc[state][5])
    
    score = cartModel(baseline_income,baseline_IncRat, baseline_loan_amount, baseline_ltv, income, credit, IncRat,loan_amount, ltv)
    # score += scoreProjection(answerUnemployment, answerRealStateGrowth)
    if score >= 30:
        return "Approved"
    else: 
        return "Declined"
    # evaluatorApplication(score)
