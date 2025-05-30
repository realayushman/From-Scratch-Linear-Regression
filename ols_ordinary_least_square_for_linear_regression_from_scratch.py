# -*- coding: utf-8 -*-
"""OLS: Ordinary Least Square for Linear regression from scratch.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vZ0UTHiXuaVtIDK_Lhx0oAv0CDnqAARw
"""

from sklearn.datasets import load_diabetes

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

x,y=load_diabetes(return_X_y=True)

print(x.shape)

print(y.shape)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=12)

reg=LinearRegression()

reg.fit(x_train,y_train)

from sklearn.metrics import r2_score

reg.intercept_

reg.coef_

r2_score(y_test,reg.predict(x_test))

x.shape

class OLS_Regressor:
  def __init__(self):
    self.coef=None
  def fit(self,x,y):
    y = np.array(y).reshape(-1, 1)
    x = np.array(x)

    ones = np.ones((x.shape[0], 1))
    x_b = np.hstack([ones, x])
    #Bi=(XT.X)inv.XTY
    x_T = x_b.T
    XTX = np.dot(x_T, x_b)
    XTX_inv = np.linalg.inv(XTX)
    XTY = np.dot(x_T, y)
    self.coef = np.dot(XTX_inv, XTY)
  def predict(self,x):
    x = np.array(x)
    ones = np.ones((x.shape[0], 1))
    X_b = np.hstack([ones, x])
    return np.dot(X_b, self.coef)

ols=OLS_Regressor()

#OLS method: 38% accuracy
#Gradient Descent method: 37.8% accuracy

ols.fit(x_train,y_train)

ols.coef

y_pred=ols.predict(x_test)
y_pred

r2_score(y_test,y_pred)

#Linear regression pf Sklearn got 38% accuracy
#My OLS implementation also got the same

#Sklearns LR internally uses OLS method, hence its exactly the same. But its more computation heavy and online learning is not practical using this method