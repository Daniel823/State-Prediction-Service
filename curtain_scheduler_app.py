#Purpose: tell the curtain what to do based on model classification

#Things to do
#1. Get state of the cutain
#2. load the model
#3. get classification
#4. update classification

# getCurtainState() return Dictionary

# updateCurtainState() return true (based on status)

# load model and predict

import os
from datetime import datetime
import observer as curtainObserver
from sklearn.externals import joblib

URL = 'http://192.168.1.119:1234'
CURRENT_DIR = 'curtain-prediction-app'
MODEL_DIR = 'model-generator/model/model.pkl'
NOW = datetime.now()

dir_path = os.path.dirname(os.path.realpath(__file__)).replace(CURRENT_DIR, MODEL_DIR)

print('Loading model from: {}'.format(dir_path))
clf = joblib.load(dir_path)

#Note: you are assuming that the place where this is running has the same time as the client
attribute  = [NOW.day, NOW.hour, NOW.minute]

print('Predicting state day:{} hour:{} min:{}'.format(NOW.day, NOW.hour, NOW.minute))
print(clf.predict([6,8,30]))
#print(curtainObserver.getState(URL))
#print(curtainObserver.updateState(URL, 0))
