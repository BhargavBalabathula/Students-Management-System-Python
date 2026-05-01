import mysql.connector
from config import DB_CONFIG
import logging

import config
print(config.__file__)

def get_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        logging.info("Database Connected")
        return conn
    except Exception as e:
        logging.error(f"DataBase Connection Error : {e}")
        raise