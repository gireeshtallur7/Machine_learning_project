import os
import sys
import pandas as pd
import numpy as np
from SOURCE.exception import Custom_Exception
import dill
from sklearn.metrics import r2_score
# from SOURCE.

def eval_model(X_train,y_train,X_test,y_test,models):
    try:
        report={}
        for i in range(len(list(models))):
            model=list(models.values())[i]
            model.fit(X_train,y_train) #traing of the models
            y_train_pred=model.predict(X_train)
            y_test_pred=model.predict(X_test)

            trained_model_score=r2_score(y_train,y_train_pred)
            test_model_score=r2_score(y_test,y_test_pred)

            report[list(models.keys())[i]]=test_model_score

            return report
    except Exception as e:
        raise Custom_Exception(e,sys)


def saved_objects(file_path,obj):

    try:
        dir_path_name=os.path.dirname(file_path)

        os.makedirs(dir_path_name,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise Custom_Exception(e,sys)
