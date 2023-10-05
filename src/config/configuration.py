import os
from pathlib import Path
from src.utils import *
from src.utils.commons import *
from src.constants import *
from src.entity.entity_config import DataIngestionConfig, PrepareBaseModelConfig
import os


class ConfigurationManager():
    def __init__(self,
                 config_file = CONFIG_FILE,
                 params_file = PARAMS_FILE):
        self.config = read_yaml(config_file)
        self.params = read_yaml(params_file)
        
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self)->DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir
        )
        return data_ingestion_config
    
    def get_base_model_config(self)->PrepareBaseModelConfig:
        config = self.config.prepare_base_model

        create_directories([config.root_dir, os.path.dirname(config.base_model_path),\
                            os.path.dirname(config.updated_model_path)])

        base_model_config = PrepareBaseModelConfig(
            root_dir = config.root_dir,
            base_model_path=config.base_model_path,
            updated_model_path = config.updated_model_path
        )

        return base_model_config