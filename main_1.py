from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation


if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    print(train_data,test_data)

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)
    print(train_arr,test_arr)