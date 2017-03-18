#Purpose: tell the curtain what to do based on model classification

#Things to do
#1. Get state of the cutain
#2. load the model
#3. get classification
#4. update classification

# getCurtainState() return Dictionary

# updateCurtainState() return true (based on status)

# load model and predict

import observer as curtainObserver
import os
from sklearn.externals import joblib

URL = 'http://192.168.1.119:1234'
CURRENT_DIR = 'curtain-prediction-app'
MODEL_DIR = 'model-generator/model/model.pkl'

dir_path = os.path.dirname(os.path.realpath(__file__)).replace(CURRENT_DIR, MODEL_DIR)

print(dir_path)
clf = joblib.load(dir_path)

print(curtainObserver.getState(URL))
print(curtainObserver.updateState(URL, 0))
