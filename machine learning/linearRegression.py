import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error

diabetes = datasets.load_diabetes()


diabetes_M = diabetes.data
diabetes_m_train = diabetes_M[:-20]
diabetes_m_test =  diabetes_M[-20:]

diabetes_n_train = diabetes.target[:-20]
diabetes_n_test = diabetes.target[-20:]

model = linear_model.LinearRegression()

model.fit(diabetes_m_train, diabetes_n_train)
diabetes_n_Predicted = model.predict(diabetes_m_test)

print("The mean Squared Error is :", mean_squared_error(diabetes_n_test, diabetes_n_Predicted))
print(" Weights:", model.coef_)
print("Intercept:", model.intercept_)
