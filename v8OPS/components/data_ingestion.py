import os
import sys
import zipfile
import urllib.request as request
from v8OPS.logger import logging
from v8OPS.exception import AppException
from dataclasses import dataclass
from v8OPS.entity.config_entity import DataIngestionConfig
from v8OPS.entity.artifacts_entity import DataIngestionArtifact


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig=DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise AppException(e, sys)
        
    def download_data(self)->str:

        try:
            dataset_url = self.data_ingestion_config.data_download_url
            zip_download_dir = self.data_ingestion_config.data_ingestion_dir
            os.makedirs(zip_download_dir, exist_ok= True)
            data_filename = "data.zip"
            zip_filepath = os.path.join(zip_download_dir,data_filename)
            logging.info(f"Downloading data from {dataset_url} into file {zip_filepath}")
            if not os.path.exists(zip_filepath):
                request.urlretrieve(
                    url = dataset_url, filename=zip_filepath
                )
                logging.info(f"{zip_filepath} downloaded!!")
            else:
                logging.info(f"File already exists on {zip_filepath}")
            
            return zip_filepath
        
        except Exception as e:
            raise AppException(e, sys)
        
    def extract_zipfile(self,zip_file_path:str)->str:
        try:
            feature_store_path = self.data_ingestion_config.feature_store_path
            os.makedirs(feature_store_path,exist_ok=True)
            with zipfile.ZipFile(zip_file_path, 'r') as zipp:
                zipp.extractall(feature_store_path)

            return feature_store_path
        
        except Exception as e:
            raise AppException(e, sys)
        

    def initiate_data_ingestion(self)-> DataIngestionArtifact:
        logging.info(f"Entered initiate_data_ingestion method of DataIngestion class")
        try:
            zip_filepath = self.download_data()
            feature_storepath = self.extract_zipfile(zip_filepath)

            data_ingestion_artifact = DataIngestionArtifact(
                data_zip_path= zip_filepath,
                feature_store_path= feature_storepath
            )

            logging.info(f"Exited initiate_data_ingestion memthod of DataIngestion class")
            logging.info(f"Data ingestion artifact: {data_ingestion_artifact}")

            return data_ingestion_artifact
        
        except Exception as e:
            raise AppException(e, sys)
        