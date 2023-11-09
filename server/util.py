import json
import pickle
import numpy as np
from functools import lru_cache
import os
import sklearn
__model = None
@lru_cache
def get_estimated_cardio(age_,gender_,height_,weight_,ap_hi,ap_lo,alco,active,smoke,glucose,cholesterol):
    x = np.zeros(11) 
    x[0] = age_
    x[1] = gender_
    x[2] = height_
    x[3] = weight_
    x[4]=ap_hi
    x[5]=ap_lo
    x[6]=cholesterol
    x[7]=glucose
    x[8]=smoke
    x[9]=alco
    x[10]=active
    return round(__model.predict([x])[0],2)
@lru_cache
def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __model
    path = os.getcwd()
    file_path = os.path.join(path, "server/artifacts/Heart_Disease_Prediction.pickle")
    with open(file_path, 'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts..done")