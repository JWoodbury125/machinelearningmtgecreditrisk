#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 21:33:19 2019

@author: nikhildikshit
"""

import pandas as pd

class Detail:

   def createBaseLine(self,year):
    # Year comes in the 
     b_year = self.df[self.df["Year"] == year]
     b_year_temp = b_year.groupby("StateName").agg(lambda x: x.value_counts().index[0])
     byear = b_year_temp[["Income" , "IncRat", "Amount"]]
     byear["Rate"] = b_year["Rate"].groupby(self.df["StateName"]).mean()
     byear["LTV"] = b_year["LTV"].groupby(self.df["StateName"]).mean()
     byear["GDP"] = b_year["GDP"].groupby(self.df["StateName"]).mean()
     byear["Unemployment"] = b_year["Unemployment"].groupby(self.df["StateName"]).mean()
     byear["Real State Growth %"] = b_year["Real State Growth %"].groupby(self.df["StateName"]).mean()
     return byear

   def __init__ (self):
     self.df = pd.read_csv('Macintosh HD⁩/⁨Users/⁨sadidasiddiqui/⁩⁨Desktop/⁨untitled folder⁩/Baseline_Dataframe.csv')
     self.baseline_2010 = self.createBaseLine(2010)
     self.baseline_2011 =  self.createBaseLine(2011)
     self.baseline_2012 =  self.createBaseLine(2012)
     self.baseline_2013 =  self.createBaseLine(2013)
     self.baseline_2014 =  self.createBaseLine(2014)
     self.baseline_2015 =  self.createBaseLine(2015)
     self.baseline_2016 =  self.createBaseLine(2016)
     self.baseline_2017 =  self.createBaseLine(2017)

     b = [self.baseline_2010, self.baseline_2011, self.baseline_2012, self.baseline_2013, self.baseline_2014, self.baseline_2015, self.baseline_2016, self.baseline_2017]
     year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
     for base,year in zip(b,year):
    
       print("Baseline profile Perstate for year: ", year)
       print(base.head())
       print("\n\n")
    
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

   def scoreLTV(income, baseline_income, ltv, baseline_ltv):
       if income > baseline_income:
          return 10
       else:
          return 5

   def cartModel(self,baseline_income,baseline_IncRat, baseline_loan_amount, baseline_ltv, income, credit, IncRat,loan_amount, ltv):
       profile_score = 0
       profile_score += self.scoreIncome(income, baseline_income)
       profile_score += self.scoreCredit(credit)
       profile_score += self.scoreIncRatio(IncRat, baseline_IncRat)
       profile_score += self.scoreLoanAmount(loan_amount, baseline_loan_amount)
       profile_score += self.scoreLTV(income, baseline_income,ltv, baseline_ltv)
       return profile_score

   def evaluatorApplication(profile_score):
       if profile_score >= 30:
          print("\nStatus: Approved")
       else:
          print("\nStatus: Declined")




#Get User details

   def getdetail(self):
    
      user_income=document.getElementById ('Income').innerText
      user_income_ratio=document.getElementById ('IncomeRatio').innerText
      user_credit_score=document.getElementById ('CreditScore').innerText
      user_loan_amount=document.getElementById ('LoanAmount').innerText
      user_LTV=document.getElementById ('LTV').innerText
      user_year=document.getElementById ('Year').innerText
      user_state=document.getElementById ('State').innerText


# Testing the Baseline Model with a application (for mortgage)
      print("\nEnter Income")
      print("\nIncome between 10000 to 400000")

      income = float(user_income)

      print("\nEnter Credit Score")
      print('\nIn between 0 to 7 Eg: 6')

      credit = int(user_credit_score)

      print("\nEnter Income Ratio")
      print("\nIn between 0 to 2 Eg: 1.27")

      IncRat = float(user_income_ratio)

      print("\nEnter Loan Amount")

      loan_amount = float(user_loan_amount)

      print("\nEnter LTV ")
      print(("\nIn between 0 to 1 Eg: 0.75"))

      ltv = float(user_LTV)

      print("\nEnter Year between 2010 and 2017")
      print('Enter year between 2018 and 2023 to get a projected status based on historical records ')

      year = int(user_year)

      print("\nEnter State")
      state = user_state

      print("\nYOU ENTER THESE -\n\nIncome as :", income,\
      "\nCredit as :", credit,\
      "\nIncome Ratio as :", IncRat,\
      "\nLoan Amount as :", loan_amount,\
      "\nLTV as :", ltv,\
      "\nYear as :", year,\
      "\nState as :", state
        )

# Feeding the above value into baseline Model
      baseline_dict = {
         2010: self.baseline_2010,\
             2011: self.baseline_2011,\
                 2012: self.baseline_2012,\
                     2013: self.baseline_2013,\
                         2014: self.baseline_2014,\
                             2015: self.baseline_2015,\
                                 2016: self.baseline_2016,\
                                     2017: self.baseline_2017
                }

      baseline_df = baseline_dict[year]
      baseline_df.loc[state]

      baseline_income       = float(baseline_df.loc[state][0])
      baseline_IncRat       = float(baseline_df.loc[state][1])
      baseline_loan_amount  = float(baseline_df.loc[state][2])
      baseline_ltv          = float(baseline_df.loc[state][5])

# basline_variable_list = [baseline_income, baseline_IncRat, baseline_loan_amount, baseline_ltv, income, credit, IncRat,loan_amount, ltv, answerUnemployment, answerRealStateGrowth]
      basline_variable_list = [baseline_income, baseline_IncRat, baseline_loan_amount, baseline_ltv, income, credit, IncRat,loan_amount, ltv]

      score = self.cartModel(baseline_income,baseline_IncRat, baseline_loan_amount, baseline_ltv, income, credit, IncRat,loan_amount, ltv)
# score += scoreProjection(answerUnemployment, answerRealStateGrowth)
      print(score)
      self.evaluatorApplication(score)
      document.getElementById ('ShowEligibility').innerHTML=score


detailinstance = Detail ()

