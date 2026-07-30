import os
import sys
from SOURCE.ulits import saved_objects,eval_model
import pandas as ps
import numpy as np
from dataclasses import dataclass
from sklearn.ensemble import AdaBoostRegressor,GradientBoostingRegressor,RandomForestRegressor
from catboost import CatBoostRegressor

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor
from SOURCE.exception import Custom_Exception
from SOURCE.logger import logging

@dataclass
class Model_Training_Config:
    trained_model_file_path=os.path.join("artifact_model","model.pkl")

class Model_Trainer:
    def __init__(self):
        self.model_trainer_config=Model_Training_Config() #inside this "model_trainer_config" variable i will get this path trained_model_file_path

    def initiate_model_trainer(self,train_array,test_array): #these all are the o/p of data  transformer
        try:
            logging.info("splitting of training and testing input data")
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            models={
                "Linear_Regressor":LinearRegression(),
                "Random_forest":RandomForestRegressor(),
                "Decision_tree":DecisionTreeRegressor(),
                "KNeighboor":KNeighborsRegressor(),
                "Gradient_Boosting":GradientBoostingRegressor(),
                "Cat_Boosting":CatBoostRegressor(verbose=False),
                "XGBoost":XGBRegressor(),
                "Adaboosting":AdaBoostRegressor()

            }

            model_report:dict=eval_model(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,models=models)

        # to get the best model score from the dectionary 
            best_model_score=max(sorted(model_report.values()))

        # to get the best model name from the dectionary
            best_model_name=list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model=models[best_model_name]

            if best_model_score<0.6:
                raise Custom_Exception("No best model found here")
            logging.info(f"best model found on the both training and testing datasets")

            saved_objects(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted=best_model.predict(X_test)
            r2_square=r2_score(y_test,predicted)
            return r2_square
        except Exception as e:
            raise Custom_Exception(e,sys)
               

