import sys
from v8OPS.logger import logging
from v8OPS.exception import AppException
from v8OPS.components.data_ingestion import DataIngestion
from v8OPS.components.data_validation import DataValidation

from v8OPS.entity.artifacts_entity import (DataIngestionArtifact,DataValidationArtifact)
from v8OPS.entity.config_entity import (DataIngestionConfig,DataValidationConfig)

class TrainingPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()

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
        
    def start_data_validation(self,data_ingestion_artifact:DataIngestionArtifact)->DataIngestionArtifact:
        logging.info("Entered start_data_validation method of the TrainPipeline class")
        try:
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact,
                                             data_validation_config=self.data_validation_config,)
            data_validation_artifact = data_validation.initiate_data_validation()
            logging.info("Exited start_data_validation method of the TrainPipeline class")

            return data_validation_artifact
        
        except Exception as e:
            raise AppException(e, sys) from e
        
    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
        
        except Exception as e:
            raise AppException(e, sys)
        

