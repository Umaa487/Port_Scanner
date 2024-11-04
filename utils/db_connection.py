from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

def get_db():
    db_conn_str = os.getenv('MongoClient')
    client = MongoClient(db_conn_str)

    db = client['PortScannerData']

    return db