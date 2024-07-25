import os 
from datetime import datetime
from dataclasses import dataclass
from v8OPS.constant import *


@dataclass
class TrainingPipelineConfig:
    artifacts_dir: str = artifacts_DIR

training_pipeline_config: TrainingPipelineConfig=TrainingPipelineConfig()

@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(
        training_pipeline_config.artifacts_dir, DATA_INGESTION_DIR
    )
    feature_store_path: str = os.path.join(
        data_ingestion_dir,DATA_INGESTION_FEATURE_STORE_DIR
    )
    data_download_url: str = DATA_DOWNLOAD_URL