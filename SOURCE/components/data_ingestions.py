import os
import sys
from SOURCE.exception import Custom_Exception
from SOURCE.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split

from dataclasses import dataclass

@dataclass
class Data_Ingestion_Config:
    train_data_path:str=os.path.join("artifect","train.csv")
    test_data_path:str=os.path.join("artifect","test.csv")
    raw_data_path:str=os.path.join("artifect","raw.csv")


class Data_ingestion:
    def __init__(self):
        self.ingestion_Config=Data_Ingestion_Config()

    def initiative_data_ingestion(self):
        logging.info("external data ingestion methods or components")
        try:
            df=pd.read_csv("students_data\stud.csv")
            logging.info("read the dataset as dataframe")
            os.makedirs(os.path.dirname(self.ingestion_Config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_Config.raw_data_path,index=False,header=True)
            logging.info("train test split initiated ")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_Config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_Config.test_data_path,index=False,header=True)    
            logging.info("ingestion of data is complited")
            return(
                    self.ingestion_Config.train_data_path,
                    self.ingestion_Config.test_data_path
            )                           
                               
        except Exception as e:
            raise Custom_Exception(e,sys)

if __name__=="__main__":
    objects=Data_ingestion()
    objects.initiative_data_ingestion()


