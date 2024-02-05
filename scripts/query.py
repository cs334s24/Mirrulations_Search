from pymongo import MongoClient

# Connection URI
uri = 'mongodb://localhost:27017'

# Database Name
dbName = 'mongoSample'

def runQuery():
    db, client = connectToMongodb()
    collection = db['file_metadata']
    # Query file counts and types
    crbCount, crbFileTypes, ihsCount, ihsDocumentsCount, ihsDocketCount, ihsFileTypes = queryFileCounts(collection)
    totalFilesCount = collection.count_documents({})
    printQueriedData(crbCount, crbFileTypes, ihsCount, ihsDocumentsCount, ihsDocketCount, ihsFileTypes, totalFilesCount)
    # Close the connection
    client.close()

# Function to connect to MongoDB
def connectToMongodb():
    client = MongoClient(uri)
    return client[dbName], client

# Function to query file counts and types from MongoDB
def queryFileCounts(collection):
    crbCount, ihsCount = 0, 0
    crbFileTypes, ihsFileTypes = {}, {}
    # Query CRB files
    crbFiles = collection.find({'main_folder': 'CRB'})
    for fileData in crbFiles:
        crbCount += 1
        fileExtension = fileData['file_extension']
        crbFileTypes[fileExtension] = crbFileTypes.get(fileExtension, 0) + 1 
    # Query IHS files
    ihsFiles = collection.find({'main_folder': 'IHS'})
    for fileData in ihsFiles:
        ihsCount += 1
        fileExtension = fileData['file_extension']
        ihsFileTypes[fileExtension] = ihsFileTypes.get(fileExtension, 0) + 1
    # Query documents and docket folders within IHS
    ihsDocumentsCount = collection.count_documents({'main_folder': 'IHS', 'file_path': {'$regex': 'documents'}})
    ihsDocketCount = collection.count_documents({'main_folder': 'IHS', 'file_path': {'$regex': 'docket'}})

    return crbCount, crbFileTypes, ihsCount, ihsDocumentsCount, ihsDocketCount, ihsFileTypes

# Function to print file type counts
def printFileTypes(fileTypes):
    for fileType, count in fileTypes.items():
        if fileType:
            print(f'{fileType}: {count}')
        else:
            print(f'file: {count}')

# Function to print the queried file counts and types
def printQueriedData(crbCount, crbFileTypes, ihsCount, ihsDocumentsCount, ihsDocketCount, ihsFileTypes, totalFilesCount):
    print('\nNumber of files in CRB:', crbCount)
    print('File types in CRB:')
    printFileTypes(crbFileTypes)
    print('\nNumber of files in IHS:', ihsCount)
    print('Number of files in "documents" folder within IHS:', ihsDocumentsCount)
    print('Number of files in "docket" folder within IHS:', ihsDocketCount)
    print('File types in IHS:')
    printFileTypes(ihsFileTypes)
    print('\nTotal number of files in the database:', totalFilesCount)

# Run the script
if __name__ == "__main__":
    runQuery()
