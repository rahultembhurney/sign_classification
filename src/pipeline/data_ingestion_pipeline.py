from src.entity.entity_config import DataIngestionConfig
from src.components.data_ingestion_component import DataIngestionComponent
from pathlib import Path
from src.config.configuration import ConfigurationManager
from src.utils.logger import logging
from src.utils.exception import CustomException
import sys


class DataIngestionPipeline():
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestionComponent(config=data_ingestion_config)


if __name__ == "__main__":
    try:
        obj = DataIngestionPipeline()
        obj.main()
        logging.info(f"DataIngestionPipeline working successfullly")
    except Exception as e:
        raise e
