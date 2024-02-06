import os
import json
from pymongo import MongoClient

# Connection URI
uri = 'mongodb://localhost:27017'

# Database Name
dbName = 'mongoSample'  # Replace 'your_database_name' with your actual database name

# Function to connect to MongoDB and ensure collections exist
def connect_to_mongodb():
    client = MongoClient(uri)
    db = client[dbName]
    # Ensure collections exist
    db.create_collection('docket')
    db.create_collection('documents')
    db.create_collection('comments')
    return db, client

# Function to insert data into collections
def insert_data(collection, data):
    collection.insert_one(data['data'])

# Function to traverse directories and insert data into MongoDB
def add_data_to_db(rootFolder, db):
    # Traverse the main folders
    for mainFolder in os.listdir(rootFolder):
        mainFolderPath = os.path.join(rootFolder, mainFolder)
        if os.path.isdir(mainFolderPath):
            # Traverse files in the folder
            for dirpath, _, filenames in os.walk(mainFolderPath):
                for filename in filenames:
                    # Get the file path
                    filePath = os.path.join(dirpath, filename)
                    # Check file extension
                    if filename.endswith('.json'):
                        # Determine the collection name based on the parent folder
                        parent_folder = os.path.basename(os.path.dirname(filePath))
                        collection_name = parent_folder.lower()
                        # Create collection if it doesn't exist
                        if collection_name not in db.list_collection_names():
                            db.create_collection(collection_name)
                        # Get collection object
                        collection = db[collection_name]
                        # Read JSON file and insert data into MongoDB
                        with open(filePath) as f:
                            data = json.load(f)
                            insert_data(collection, data)

# Run the script
if __name__ == "__main__":
    db, client = connect_to_mongodb()
    add_data_to_db('sample-data', db)  # Replace the path with the actual path to your root folder
    client.close()
