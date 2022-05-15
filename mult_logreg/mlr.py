import csv
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression



training = pd.read_csv('filename').to_numpy()
training_x, training_y = training.iloc[:,:-1], training.iloc[:,-1] 
testing = pd.read_csv('filename').to_numpy()
testing_x, testing_y = testing.iloc[:,:-1], testing.iloc[:,-1] 


logreg = LogisticRegression(multi_class='multinomial', solver='lbfgs')
logreg.fit(training_x, training_y)

train_acc = np.count_nonzero(logreg.predict(training_x) == training_y) / len(training_y)
print(train_acc)

test_y_hat = logreg.predict(testing_x)
test_acc =  np.count_nonzero(logreg.predict(testing_x) == testing_y) / len(testing_y)
print(test_acc)




