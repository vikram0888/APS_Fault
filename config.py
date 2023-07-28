#project configuration #common configuration details defined here

from dataclassess import dataclass
import os
omport pymongo

MONGO_DB_URL_ENV_KEY = "MONGO_DB_URL"

@dataclass
class EnvironmentVariable:
    mongo_db_url:str =os.getenv("MONGO_DB_URL_ENV_KEY")

env_var= EnvironmentVariable() #creating object of the above class
mongo_client=pymongo.MongoClient(env_var.mongo_db_url) #connector which connect to mongoDB database