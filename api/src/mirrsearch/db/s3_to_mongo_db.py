""" This script connects to MongoDB and inserts data into collections """

# pylint: disable=too-many-nested-blocks, unspecified-encoding
# pylint: disable=consider-using-from-import
# pylint: disable=used-before-assignment

import os
import json
import sys
import boto3
from pymongo import MongoClient
import mirrsearch.db.mongo_db as mongo_db


def connect_to_mongodb(uri):
    """ Function to connect to MongoDB and ensure collections exist """
    client = MongoClient(uri)
    if 'mirrsearch' not in client.list_database_names():
        database = client['mirrsearch']
        database.create_collection('docket')
        database.create_collection('documents')
        database.create_collection('comments')
    else:
        database = client['mirrsearch']
    return database, client


def pull_data_from_s3(agency):
    """ Function to pull data from S3 """
    s3 = boto3.resource(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name=os.getenv('AWS_REGION')
    )
    bucket = s3.Bucket('mirrulations')
    for obj in bucket.objects.filter(Prefix=agency):
        if (obj.key.endswith('.json') or obj.key.endswith('.txt') or obj.key.endswith('.htm')):
            bucket.download_file(obj.key, obj.key.split('/')[-1])
            add_data_to_database(obj.key, database)
            os.remove(obj.key.split('/')[-1])


# This function is currently bypassing utf-8 encoding errors by ignoring them for .htm files
# This is not a good solution, but it is a temporary fix for the time being
def insert_docket_file(file, collection, docket_id):
    """ Function to insert a JSON or HTM file into a collection """
    if file.endswith('.json'):
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            mongo_db.insert_json_data(collection, data)
            print('inserted json data: ', file)
    if file.endswith('.txt'):
        with open(file, 'r', encoding='utf-8') as f:
            data = f.read()
            mongo_db.insert_txt_data(collection, data, docket_id)
            print('inserted txt data: ', file)
    if file.endswith('.htm'):
        # The below line is a temporary fix for the time being to get .htm files loaded
        with open(file, 'r', encoding='utf-8', errors="ignore") as f:
            data = f.read()
            mongo_db.insert_txt_data(collection, data, docket_id)
            print('inserted htm data: ', file)


def add_data_to_database(root, database):
    """ Function to add data to the database """
    file = root.split('/')[-1]
    if root.split('/')[-2] == 'docket':
        if file.endswith('.json') or file.endswith('.txt') or file.endswith('.htm'):
            docket_id = root.split('/')[-4]
            insert_docket_file(file, database['docket'], docket_id)
    if root.split('/')[-2] == 'comments':
        if file.endswith('.json') or file.endswith('.txt') or file.endswith('.htm'):
            docket_id = root.split('/')[-4]
            insert_docket_file(file, database['comments'], docket_id)
    if root.split('/')[-2] == 'documents':
        if file.endswith('.json') or file.endswith('.txt') or file.endswith('.htm'):
            docket_id = root.split('/')[-4]
            insert_docket_file(file, database['documents'], docket_id)


if __name__ == "__main__":
    agency = sys.argv[1]
    URI = 'mongodb://localhost:27017'
    database, client = connect_to_mongodb(URI)
    if agency.lower() == 'reset':
        database = mongo_db.clear_db(client)
        client.close()
        sys.exit()
    pull_data_from_s3(agency)
    client.close()
