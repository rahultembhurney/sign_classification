import os
from src.entity.entity_config import DataIngestionConfig
from src.config.configuration import ConfigurationManager
from pathlib import Path

class DataIngestionComponent():
    def __init__(self, config:DataIngestionConfig):
        self.config = config
        print(f"Invoker data ingestion component")

    