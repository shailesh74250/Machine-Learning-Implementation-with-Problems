#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Simple Linear Regression
Created on Mon Mar 19 00:21:44 2018

@author: shailesh
"""
# importing library
import pandas as pd

# importing dataset
dataset = pd.read_csv('Salary_Data.csv')

# extracting features dependent and independent variables
x = dataset.iloc[:,:-1]
y = dataset.iloc[:,1]

# splitting the dataset into the Training set and Testing set
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = .2, random_state = 0)


