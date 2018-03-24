#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Data - Preprocessing
Created on Sun Mar 18 23:14:20 2018
@author: Shailesh
"""
# reading dataset
import pandas as pd  # it is tool for manipulating data and data analysis
dataset = pd.read_csv('Data.csv')

# separating dataset independent and dependent variable
x = dataset.iloc[:,:-1]
y = dataset.iloc[:, 3]






