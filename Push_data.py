import os
import sys
import json

from dotenv import load_dotenv

load_dotenv()

Mongo_db_url = os.getenv("Mongo_DB_url")
print(Mongo_db_url)

import certifi
ca =certifi.where()

import pandas as pd
import numpy as np
import pymongo
from Networksecurity.Exception.exception import NetworkSecurityException
from Networksecurity.Logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def cv_to_json_convertor(self,file_path):
        try:
            data =pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records

            self.mongo_client = pymongo.MongoClient(Mongo_db_url)
            self.database = self.mongo_client[self.database]

            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return(len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e,sys)

if __name__=='__main__':
    File_path = "Network_data/phisingData.csv"
    Database = "Bhuvi"
    Collection="NetworkData"
    networkobj=NetworkDataExtract()
    records = networkobj.cv_to_json_convertor(file_path=File_path)
    print(records)
    no_of_records=networkobj.insert_data_mongodb(records,Database, Collection)
    print(no_of_records)