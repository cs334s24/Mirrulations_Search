# Pagination Documentation

## What is Pagination

Pagination is a process of dividing data into discrete pages, allowing users to view a specific subset of data at a time. This will be useful when we switch to a large data set, as it will reduce the amount of data transferred at once and improve the response times.

## Cursor-based pagination

Cursor-based pagination works by using a unique identifier (a cursor) from the currently loaded data set to fetch the next or previous set of records. This method is especially efficient for large data sets because it doesn't require the server to count or skip through a potentially large number of records to find the starting point of the desired page.

## Implementing Pagination

Modify the search_dockets method to accept two new parameters: last_id and limit. last_id is the cursor indicating where the last query stopped, and limit is the maximum number of results to return

Modify MongoManager 

```
def search_dockets(self, search_term):

    query_filter = {'attributes.title': {'$regex': f'{search_term}'}}

    if last_id:
        query_filter['_id'] = {'$gt': last_id}
    
    query = dockets.find(query_filter).limit(limit).sort('_id', 1)

```

Modify QueryManager

```
def search_dockets(self, search_term, last_id=None, limit=10):

    search = self._manager.search_dockets(search_term, last_id, limit)
```

Modify API Endpoint

```
    @app.route('/search_dockets')
    def search_dockets():

        search_term = request.args.get('term')
        last_id = request.args.get('last_id', None)
        limit = request.args.get('limit', 10, type=int)

        response = query_manager.search_dockets(search_term, last_id, limit)
        return jsonify(response)
```


