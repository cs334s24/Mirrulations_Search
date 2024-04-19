""" This script connects to MongoDB and inserts data into collections """

# pylint: disable=too-many-nested-blocks, unspecified-encoding
# pylint: disable=unused-variable, used-before-assignment

import os
import json
import sys
from pymongo import MongoClient


def connect_to_mongodb(uri):
    """ Function to connect to MongoDB and ensure collections exist """
    client = MongoClient(uri)
    database = clear_db(client)
    return database, client


def clear_db(client):
    """ Function to clear all collections in the database """
    database = client['mirrsearch']
    for collection in database.list_collection_names():
        database[collection].drop()
    database.create_collection('docket')
    database.create_collection('documents')
    database.create_collection('comments')
    return database


def insert_json_data(collection, data):
    """ Function to insert data into collections """
    collection.insert_one(data['data'])


def insert_txt_data(collection, data, docket_id):
    """ Function to insert data into collections """
    collection.insert_one({'id':docket_id, 'data': data})


# This function is currently bypassing utf-8 encoding errors by ignoring them for .htm files
# This is not a good solution, but it is a temporary fix for the time being
def insert_docket_file(file, collection, docket_id):
    """ Function to insert a JSON or HTM file into a collection """
    if file.endswith('.json'):
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            insert_json_data(collection, data)
    if file.endswith('.txt'):
        with open(file, 'r', encoding='utf-8') as f:
            data = f.read()
            insert_txt_data(collection, data, docket_id)
    if file.endswith('.htm'):
        # The below line is a temporary fix for the time being to get .htm files loaded
        with open(file, 'r', encoding='utf-8', errors="ignore") as f:
            data = f.read()
            insert_txt_data(collection, data, docket_id)


def add_data_to_database(root_folder, database):
    """ Function to add data to the database """
    for root, _, files in os.walk(root_folder):
        if root.split('/')[-1] == 'docket':
            for file in files:
                if file.endswith('.json') or file.endswith('.txt') or file.endswith('.htm'):
                    docket_id = root.split('/')[-3]
                    insert_docket_file(os.path.join(root, file), database['docket'], docket_id)
        if root.split('/')[-1] == 'comments':
            for file in files:
                if file.endswith('.json') or file.endswith('.txt') or file.endswith('.htm'):
                    docket_id = root.split('/')[-3]
                    insert_docket_file(os.path.join(root, file), database['comments'], docket_id)
        if root.split('/')[-1] == 'documents':
            for file in files:
                if file.endswith('.json') or file.endswith('.txt') or file.endswith('.htm'):
                    docket_id = root.split('/')[-3]
                    insert_docket_file(os.path.join(root, file), database['documents'], docket_id)


if __name__ == "__main__":
    data_folder = sys.argv[1]
    MONGO_URI = 'mongodb://localhost:27017'
    database, client = connect_to_mongodb(MONGO_URI)
    add_data_to_database(data_folder, database)
    client.close()
