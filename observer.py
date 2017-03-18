import requests
import json
import sys
import os

def getState(url):
    try:
        r = requests.get('{}/state'.format(url))
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        return None

    return json.loads(r.json())

def updateState(url, state):
    try:
        r = requests.post('{}/update/{}/'.format(url, state))
        if(r.status_code == 200):
            return True
        else:
            print(r.status_code)
            return False
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        return False
