import os
import sys
import numpy as np
import pandas as pd
from SOURCE.exception import Custom_Exception
from SOURCE.logger import logging
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.impute import SimpleImputer
from dataclasses import dataclass
from sklearn.pipeline import Pipeline

from SOURCE.ulits import saved_objects

@dataclass
class Data_transformation_config:
    preprocessor_obj_file_path=os.path.join("artifacts","preprocessor.pkl")

class Data_transformation:
    def __init__(self):
        self.data_transmission_config=Data_transformation_config()

    def get_data_transform_object(self):
        '''
            this "get_data_transform_object" function is responsible for data transformation based on diff types of data
        '''
        try:
            numeric_cols=['reading_score','writing_score']
            categoric_cols=["gender",
            "race_ethnicity",
            "parental_level_of_education",
            "lunch",
            "test_preparation_course"
            ]

            # oh_encode=OneHotEncoder()
            # std_scl=StandardScaler()
            # sim_imp=SimpleImputer()

            numeric_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")),
                     ("std_scaler",StandardScaler())
                ]
            )# this pipeline is to run on the training data set (fit.transfoem(X_train))
            categorical_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")),
                     ("one_hot_encode",OneHotEncoder()),
                     ("std_scaling",StandardScaler(with_mean=False))
                ]
            )
            logging.info(f"numericals columns standard scaling complited : {numeric_cols}")

            logging.info(f"categorical columns encoding completed : {categoric_cols}")

            prepocessor=ColumnTransformer(
                [
                    ("numerical_pipeline",numeric_pipeline,numeric_cols),
                    ("categorical_pipeline",categorical_pipeline,categoric_cols)
                ]
            )# this is the combination of both numeric & categorical pipeline

            return prepocessor


        except Exception as e:
            raise Custom_Exception(e,sys)
        
    #now i will start  my data transformation inside this below func
    def  initiate_data_transform(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("read train and test data completed")
            logging.info("obtaing preprocessing objects")

            preprocessor_obj=self.get_data_transform_object()

            target_col_name="math_score"
            numeric_cols=['reading_score','writing_score']

            input_feature_train_df=train_df.drop(columns=[target_col_name],axis=1)
            target_feature_train_df=train_df[target_col_name]

            input_feature_test_df=test_df.drop(columns=[target_col_name],axis=1)
            target_feature_test_df=test_df[target_col_name]

            logging.info(f"applying preprocessing object on traing and testing dataframe")

            input_feature_train_arr=preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessor_obj.transform(input_feature_test_df)

            train_arr=np.c_[
                input_feature_train_arr,np.array(target_feature_train_df)
            ]
            test_arr=np.c_[input_feature_test_arr,np.array(target_feature_test_df)]

            logging.info("saved the preprocessing objects")

            saved_objects(
                file_path=self.data_transmission_config.preprocessor_obj_file_path,
                obj=preprocessor_obj
            ) #just for saving the pickle file


            return (

                train_arr,
                test_arr,
                self.data_transmission_config.preprocessor_obj_file_path



            )

        except Exception as e:
            raise Custom_Exception(e,sys)

            

