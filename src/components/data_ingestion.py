import os 
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd


from sklearn.model_selection import train_test_split
from dataclasses import dataclass

#print(os.getcwd())
@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts',"train.csv")
    test_data_path:str=os.path.join('artifacts',"test.csv")
    raw_data_path:str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data Ingestion Method")
        try:
            df=pd.read_csv('Notebook/Data/stud.csv')
            logging.info('Read the Dataset')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,header=True,index=False)

            logging.info("Train Test Split Initiated")

            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,header=True,index=False)
            test_set.to_csv(self.ingestion_config.test_data_path,header=True,index=False)

            logging.info('Ingestion is completed')

            return (
                self.ingestion_config.train_data_path,self.ingestion_config.test_data_path
            )
        
        except Exception as e:
            raise CustomException(e,sys)


        




