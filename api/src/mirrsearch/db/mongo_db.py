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
    db = client[DB_NAME]
    # Ensure collections exist
    db.create_collection('docket')
    db.create_collection('documents')
    db.create_collection('comments')
    return db, client

def insert_data(collection, data):
    """ Function to insert data into collections """
    collection.insert_one(data['data'])

def add_data_to_db(root_folder, db):
    """ Function to traverse directories and insert data into MongoDB """
    # Traverse the main folders
    for main_folder in os.listdir(root_folder):
        main_folder_path = os.path.join(root_folder, main_folder)
        if os.path.isdir(main_folder_path):
            # Traverse files in the folder
            for dirpath, _, filenames in os.walk(main_folder_path):
                for filename in filenames:
                    # Get the file path
                    file_path = os.path.join(dirpath, filename)
                    # Check file extension
                    if filename.endswith('.json'):
                        # Determine the collection name based on the parent folder
                        parent_folder = os.path.basename(os.path.dirname(file_path))
                        collection_name = parent_folder.lower()
                        # Create collection if it doesn't exist
                        if collection_name not in db.list_collection_names():
                            db.create_collection(collection_name)
                        # Get collection object
                        collection = db[collection_name]
                        # Read JSON file and insert data into MongoDB
                        with open(file_path, "r") as f:
                            data = json.load(f)
                            insert_data(collection, data)

# Run the script
if __name__ == "__main__":
    db, client = connect_to_mongodb()
    add_data_to_db('sample-data', db)
    client.close()
