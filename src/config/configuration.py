import os
from pathlib_1 import Path
from src.utils import *
from src.utils.commons import *
from src.constants import *

class ConfigurationManager():
    def __init__(self,
                 config_file = CONFIG_FILE,
                 params_file = PARAMS_FILE):
        self.config = read_yaml(config_file)
        self.params = read_yaml(params_file)
        
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self):
        config = self.config.data_ingestion

        create_directories([config.root_dir])