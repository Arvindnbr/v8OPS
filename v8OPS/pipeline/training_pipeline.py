import sys, os
from v8OPS.logger import logging
from v8OPS.exception import AppException
from v8OPS.components.data_ingestion import DataIngestion

from v8OPS.entity.artifacts_entity import (DataIngestionArtifact)
from v8OPS.entity.config_entity import (DataIngestionConfig)

class TrainingPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            logging.info("Started data ingestion method of training pipeline")
            logging.info("Getting data from the url")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("extracted data from URL")
            logging.info("Exited the start_data_ingestion method of the TrainingPipeline class")
            return data_ingestion_artifact
        except Exception as e:
            raise AppException(e, sys)
        
    def run_pipeline(self)->None:
        try:
            data_ingstion_artifact = self.start_data_ingestion()
        
        except Exception as e:
            raise AppException(e, sys)
