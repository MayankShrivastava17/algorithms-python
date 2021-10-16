"""Implementation of SVM Algorithm Using Python - By Shubham Jha
"""

from sklearn import svm, datasets
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import accuracy_score 
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()

X = iris.data[:, :12] # we will take twelve features
y = iris.target
x_train, x_test, y_train, y_test = train_test_split(X, y, random_state = 0, test_size = 0.25)

clf = svm.SVC(kernel='linear', C=1).fit(x_train, y_train)

import pandas as pd
Iris = pd.read_csv("/content/train_qnU1GcL.csv")
Iris.head(20)

classifier_predictions = clf.predict(x_test)
print(accuracy_score(y_test, classifier_predictions)*100)


#Accuracy of this model is - 97.36842105263158
