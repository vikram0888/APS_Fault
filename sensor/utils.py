from .config import mongo_client
import pandas as pd
import logging

#dump csv file in mongoDB
def dump_csv_file_to_mongodb_collection(file_path:str,database:str, collection_name:str)->None:
    try:
        #reading csv file
        df =pd.read_csv(file_path)
        logging.info(f"Rows and Colums (df.shape)")
        
        #drop index
        df.reset_index(drop=True, inplace=True)
        
        #transform into json format 
        json_records = list(json.loads(df.T.to_json()).values()) #json.loads((df.T.to_json()).values())--> generator
        mongo_client[database_name][collection_name].insert_many(json_records)
    except Exception as e:
        raise e