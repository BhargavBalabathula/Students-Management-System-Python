from logger_config import setup_logger
from gui import run_app
import logging

setup_logger()
logging.info("Application Started")

run_app()