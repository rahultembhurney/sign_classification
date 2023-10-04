import yaml
import joblib
import json
import os
from box import ConfigBox
from pathlib import Path
import sys
from src.utils import logger
from src.utils.exception import CustomException
import logging
import os
import joblib

def read_yaml(filepath):
    '''
    Reads a YAML file and returns its contents

    ARGS:
        filepath (str): Path of YAML file

    Raises:
        ValueError: Check logs

    Returns:
        ConfigBox: ConfigBox type
    '''
    try:
        logging.info(f"Reading YAML file")

        with open(filepath, "r") as f:
            context = yaml.safe_load(f)

        logging.info(f"{filepath} read succesful return configbox")
        return ConfigBox(context)
    
    except Exception as e:
        logging.info(f"{CustomException(e, sys)}")
        raise CustomException(e, sys)
    

def create_directories(filepaths: list):
    '''
    Creates Directory for the list of paths

    ARGS:
        filepaths (list): list of paths of files

    Raises:
        Check logs for errors
    '''
    try:
        for f in filepaths:
            logging.info(f"creating directory {f}")
            os.makedirs(f, exist_ok=True)
            logging.info(f"directory {f} created successfully")
    
    except CustomException as e:
        logging.info(f"{CustomException(e, sys)}")
        raise CustomException(e, sys)
    

def save_model(filepath, model):
    '''
    Saves the model at given path

    ARGS:
        filepath (Path): Path to save the model

        model (Any): Model to save
    
    RAISES:
        Check logs for error
    '''
    try:
        logging.info(f"Saving {model} to path {filepath}")
        joblib.dump(value=model, filename=filepath)
        logging.info(f"{model} saved Successfully")

    except CustomException as e:
        logging.info(f"{CustomException(e, sys)}")
        raise CustomException(e, sys)
    

def load_model(filepath, model):
    '''
    Loads the model from given path

    ARGS:
        filepath (Path): Path to load model from

        model (Any): Model to load
    
    RAISES:
        Check logs for error
    '''
    try:
        logging.info(f"Loading {model} from path {filepath}")
        joblib.load(value=model, filename=filepath)
        logging.info(f"{model} loaded Successfully")
        
    except CustomException as e:
        logging.info(f"{CustomException(e, sys)}")
        raise CustomException(e, sys)

    


