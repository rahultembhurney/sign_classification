import os
from datetime import datetime
import logging

LOGFILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
LOGFILE_PATH = os.path.join(os.getcwd(), "logs", LOGFILE)
os.makedirs(LOGFILE_PATH, exist_ok=True)

LOG_FOLDER = os.path.join(LOGFILE_PATH, LOGFILE)
FORMAT = "[%(asctime)s]- %(lineno)s- %(levelname)s- %(message)s]"

logging.basicConfig(
    filename=LOG_FOLDER,
    format=FORMAT,
    level=logging.INFO,
)


if __name__ == "__main__":
    logging.info(f"logging.py running successfully")