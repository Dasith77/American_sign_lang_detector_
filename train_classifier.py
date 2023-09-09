import pickle

# do the training using random forest
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

from create_dataset import class_lables

data_dict = pickle.load(open('./data.pickle', 'rb'))

data = np.asarray(data_dict['data'])
labels = np.asarray(data_dict['labels'])  # Use 'labels' key instead of 'class_labels'

# divide data sets into training and test sets
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.4, shuffle=True,
                                                    stratify=labels)

# create the model
model = RandomForestClassifier()

model.fit(x_train, y_train)

y_predict = model.predict(x_test)

score = accuracy_score(y_predict, y_test)

print('{}% of samples were classified correctly !'.format(score * 100))

# create file to save all this data
with open('model.p', 'wb') as f:
    pickle.dump({'model': model}, f)
f.close()
