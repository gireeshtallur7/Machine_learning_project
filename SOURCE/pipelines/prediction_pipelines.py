import os
import sys
import pandas as pd
from SOURCE.exception import Custom_Exception
from SOURCE.ulits import load_object

class PredictPipeline:
    def __init__(self):
        pass
    def model_prediction(self,features): #prediciton of my model
        try:
            model_path=os.path.join("artifact_model", "model.pkl")
            preprocessor_path=os.path.join("artifacts", "preprocessor.pkl")
            model=load_object(file_path=model_path) # this load_object will import the pickel and load the pickel file
            preprocessor=load_object(file_path=preprocessor_path)

            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        except Exception as e:
            raise Custom_Exception(e,sys)
    


class Custom_Data: # this class will work as backend for collected input data from the user
    def __init__(self,
                 gender:str, race_ethnicity:str, parental_level_of_education:str,
                lunch:str,test_preparation_course:str, reading_score:int, writing_score:int):
        self.gender=gender
        self.race_ethnicity=race_ethnicity
        self.parental_level_of_education=parental_level_of_education
        self.lunch=lunch
        self.test_preparation_course=test_preparation_course
        self.reading_score=reading_score
        self.writing_score=writing_score


    def get_data_as_DataFrame(self):
        try:
            custom_data_input_dict= {
                'gender':[self.gender],
                'race_ethnicity':[self.race_ethnicity],
                'parental_level_of_education':[self.parental_level_of_education],
                'lunch':[self.lunch],
                'test_preparation_course':[self.test_preparation_course],
                'reading_score':[self.reading_score],
                'writing_score':[self.writing_score]
            }

            return pd.DataFrame(custom_data_input_dict)


        except Exception as e: 
            raise Custom_Exception(e,sys)


        

        

        

        
        
