import os,sys
from v8OPS.logger import logging
from v8OPS.exception import AppException
from v8OPS.entity.config_entity import DataValidationConfig
from v8OPS.entity.artifacts_entity import (DataIngestionArtifact,DataValidationArtifact)




class DataValidation:
    def __init__(self, data_ingestion_artifact: DataIngestionArtifact, data_validation_config: DataValidationConfig,):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config

        except Exception as e:
            raise AppException(e, sys)

    
    def validate_all_files_exist(self)->bool:
        try:
            validation_status = None
            total_files = os.listdir(self.data_ingestion_artifact.feature_store_path)

            for file in total_files:
                if file not in self.data_validation_config.required_filelist:
                    validation_status = False
                    os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
                    with open(self.data_validation_config.validation_statusfile_dir, 'w') as boo:
                        boo.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
                    with open(self.data_validation_config.validation_statusfile_dir, 'w') as boo:
                        boo.write(f"Validation status: {validation_status}")
            return validation_status
        
        except Exception as e:
            raise AppException(e, sys)
        

    def initiate_data_validation(self) -> DataValidationArtifact:
        logging.info("Entered initiate_data_validation method of DataValidation class")
        try:
            status = self.validate_all_files_exist()
            data_validation_artifact = DataValidationArtifact( validation_status= status)
            logging.info("Exited initiate_data_validation method of DataValidation class")
            logging.info(f"Data validation Artifact: {data_validation_artifact}")

        except Exception as e :
            raise AppException(e, sys)


