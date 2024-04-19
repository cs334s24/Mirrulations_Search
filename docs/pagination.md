# Pagination Documentation

## What is Pagination

Pagination is a process of dividing data into discrete pages, allowing users to view a specific subset of data at a time. This will be useful when we switch to a large data set, as it will reduce the amount of data transferred at once and improve the response times.

## Example Queries

The below examples are for the search term Indian and the IHS agency
Currently this search term returns 33 results

* query for page 1
```
curl 'localhost:8000/search_dockets?term=Indian&page=1'
```

Will return results 1-10

* query for page 2
```
curl 'localhost:8000/search_dockets?term=Indian&page=2'
```

Will return results 11-20

* query with no page parameter
```
curl 'localhost:8000/search_dockets?term=Indian'
```

This will deafault to page 1 if not given a page parameter

* query for last page
```
curl 'localhost:8000/search_dockets?term=Indian&page=4'
```

Will return results 31-33

* query out of bounds
```
curl 'localhost:8000/search_dockets?term=Indian&page=5'
```

Will return nothing












