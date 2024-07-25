from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    data_zip_path: str 
    feature_store_path: str 
@dataclass
class DataValidationArtifact:
    validation_status: bool



#data zip file path
#feature store path

#Data validation dataclass

