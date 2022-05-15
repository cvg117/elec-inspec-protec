import csv
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression



county_arr = pd.read_csv('../data/mi_matched_county.csv').to_numpy()
training, testing = train_test_split(county_arr)
training_x, training_y = training[:,:-1], training[:,-1]
testing_x, testing_y = testing[:,:-1], testing[:,-1] 


logreg = LogisticRegression(multi_class='multinomial', solver='lbfgs')
logreg.fit(training_x, training_y)

train_acc = np.count_nonzero(logreg.predict(training_x) == training_y) / len(training_y)
print(train_acc)

test_y_hat = logreg.predict(testing_x)
test_acc =  np.count_nonzero(logreg.predict(testing_x) == testing_y) / len(testing_y)
print(test_acc)




