import os
from pymongo import MongoClient

# Connection URI
uri = 'mongodb://localhost:27017'

# Database Name
dbName = 'mongoSample'

# Function to connect to MongoDB
def connectToMongodb():
    client = MongoClient(uri)
    return client[dbName], client

# Function to insert file metadata into MongoDB
def insertFileMetadata(collection, mainFolder, filePath, fileSize, fileExtension):
    collection.insert_one({
        'main_folder': mainFolder,
        'file_path': filePath,
        'file_size': fileSize,
        'file_extension': fileExtension
    })

# Function to check if a file already exists in the database
def checkIfFileExists(collection, filePath):
    return collection.count_documents({'file_path': filePath}) > 0

# Function to traverse directories and insert data into MongoDB
def addDataToDB(rootFolder):
    # Connect to MongoDB
    db, client = connectToMongodb()
    collection = db['file_metadata']
    # Counter for number of new files added
    newFilesAdded = 0
    # Traverse the main folders
    for mainFolder in os.listdir(rootFolder):
        mainFolderPath = os.path.join(rootFolder, mainFolder)
        if os.path.isdir(mainFolderPath):
            newFilesAdded += processMainFolder(mainFolder, mainFolderPath, collection)
    # Close the connection
    client.close()
    print(f'Number of new files added: {newFilesAdded}')

# Function to process files within a main folder
def processMainFolder(mainFolder, mainFolderPath, collection):
    newFilesAdded = 0
    for dirpath, _, filenames in os.walk(mainFolderPath):
        for filename in filenames:
            # Get the file path
            filePath = os.path.join(dirpath, filename)
            # Check if file already exists in the database
            if not checkIfFileExists(collection, filePath):
                # Get file size
                fileSize = os.path.getsize(filePath)
                # Get file extension
                fileExtension = os.path.splitext(filename)[1]
                # Insert metadata into the MongoDB collection
                insertFileMetadata(collection, mainFolder, filePath, fileSize, fileExtension)
                newFilesAdded += 1
    return newFilesAdded

# Run the script
if __name__ == "__main__":
    addDataToDB('sample-data')
