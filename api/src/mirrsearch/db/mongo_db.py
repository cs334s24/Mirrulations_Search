""" This script connects to MongoDB and inserts data into collections """

# pylint: disable=too-many-nested-blocks, unspecified-encoding

import os
import json
from pymongo import MongoClient

# Connection URI
URI = 'mongodb://localhost:27017'

# Database Name
DB_NAME = 'mongoSample'

def connect_to_mongodb():
    """ Function to connect to MongoDB and ensure collections exist """
    client = MongoClient(URI)
    database = client[DB_NAME]

    clear_db(database)
    database.create_collection('docket')
    database.create_collection('documents')
    database.create_collection('comments')
    return database, client

def insert_data(collection, data):
    """ Function to insert data into collections """
    collection.insert_one(data['data'])


def add_data_to_database(root_folder, database):
    """ Function to add data to the database """
    docket_ids = get_list_of_dockets()
    for docket_id in docket_ids:
        for root, _, files in os.walk(root_folder):
            for file in files:
                if file == f'{docket_id}.json':
                    with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        insert_data(database['docket'], data)
                        if 'documents' in data['data']:
                            for document in data['data']['documents']:
                                insert_data(database['documents'], document)
                                if 'comments' in document:
                                    for comment in document['comments']:
                                        insert_data(database['comments'], comment)



def clear_db(database):
    """ Function to clear all collections in the database """
    for collection in database.list_collection_names():
        database[collection].drop()


def get_list_of_dockets():
    """ Function to get a list of all dockets """
    docket_list = []
    for root, _, files in os.walk('sample-data'):
        for file in files:
            if file.endswith('.json'):
                file = file[:-5]
                docket_list.append(file)
    return docket_list


if __name__ == "__main__":
    database, client = connect_to_mongodb()
    add_data_to_database('sample-data', database)
    client.close()
