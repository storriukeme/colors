import numpy as np
from settings import logger
import os
from dotenv import load_dotenv

load_dotenv()

def get_color():
    logger.info(f"sub module requirements.txt works {type(np.array([2, 3, 4]))}")
    logger.info(f"the secret is {os.environ['MYSECRET']} ")
    return "Red"

