from mirrsearch.api.mongo_manager import MongoManager

class MongoQueries:

    # __manager = None

    def search_dockets(search_term):
        response = {}

        # Establishes connection to the dockets collection
        manager = MongoManager()
        client = manager.get_instance()
        db = client['mongoSample']
        dockets = db.get_collection('docket')

        # Query to get term within docket title, NOTE: it is case sensitive currently
        search = dockets.find({'attributes.title': {'$regex': f'{search_term}'}})
            
        # If the search term is valid, data will be ingested into the JSON response
        response['data'] = {
            'search_term': search_term,
                'dockets': []
            }

        for doc in search:
            title = doc['attributes']['title']
            id = doc['id']
            link = doc['links']['self']
            # TODO: Query comments and documents collections to get count of each using docket ID
            number_of_comments = 0
            number_of_documents = 0
            response['data']['dockets'].append({
                'title': title,
                'id': id,
                'link': link,
                'number_of_comments': number_of_comments,
                'number_of_documents': number_of_documents
            })
                
        manager.close_instance()

        return response
    
    # def __init__(self):
    #     MongoQueries.__manager = MongoManager()
