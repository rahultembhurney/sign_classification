import os
from src.entity.entity_config import DataIngestionConfig
from src.config.configuration import ConfigurationManager


class DataIngestionComponent():
    def __init__(self, config:DataIngestionConfig):
        self.config = config
        print(f"Invoked DataIngestionComponent")

    