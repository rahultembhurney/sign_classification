import logging
from src.utils import logger
import sys

def error_details(error, error_details:sys):
    _,_,execution_info = error_details.exc_info()
    filename = execution_info.tb_frame.f_code.co_filename()
    lineno = execution_info.tb_lineno()
    error_message = f"Error occured in filename {filename}\
        line no {lineno} message {error}"
    
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_details:sys):
        super().__init__()
        self.error_message = error_details(error_message, error_details)

    def __str__(self):
        return self.error_message
    


if __name__ =="__main__":
    try:
        logging.info(f"exception.py successfully running")
    except Exception as e:
        logging.info(f"{CustomException(e, sys)}")
        raise CustomException(e, sys)