# API Documentation

## /search_dockets
### Description
The name for this API endpoint will be `/search_dockets`. This endpoint will be used to search our database for dockets that contain the specified term and will return all dockets that contain it. Within the dockets, specific comments and documents that contain that term will also be specified. 

### Calling the Endpoint
`/search_dockets?term=SEARCH_PARAMETER`<br>
To call the endpoint, hit the example API call above and replace the `term` query parameter with the term the caller wants to search for. The endoint will process the query parameter and interact with our backend database respectively.

#### Parameters
`term` - String that contains the search term the user wishes to query.

### Endpoint Return
All API calls will return a JSON response type that contains each docket that has the keyword within it. <br>

* `200`<br>
```
{
  "data": {
    "dockets": [
      {
        "comment_date_range": "string",
        "comments_containing": "integer",
        "docket_agency": "string",
        "docket_type": "string",
        "documents_containing": "integer",
        "id": "string",
        "link": "string",
        "title": "string",
        "total_comments": "integer",
        "total_documents": "integer"
      },
    ]
  },
  "meta": {
    "links": {
      "current": "string",
      "first": "string",
      "last": "string",
      "next": "string"
    },
    "total_results": "integer"
  }
}
```
The response above will be returned for every API call with a 200 status code. All dockets relevant to the search will be formatted in a list. Within each docket object is relevant information such as the number of comments and the number of documents that are contained within the docket. A link for each search hit will be returned as well that leads the user to the relevant docket on regulations.gov. 

* 400
```
{
    "error": {
        "code": "integer",
        "message": "string"
    }
}
```
The response above will be returned for every API call with a 400 status code. If the caller does not provide a search term, the server will return a 400 error because the term was not found.

## /search_documents
### Description
The name for the API endpoint will be '/search_documents'. This endpoint will be used to search our database for documents that contain the specified term and will return all documents that contain 
it.

### Calling the Endpoint
`/search_documents?term=SEARCH_PARAMETER&docket_id=IDNUMBER`<br>
To call the endpoint, hit the example API call above and replace the `term` query parameter with the term the caller wants to search for. The endoint will process the query parameter and interact 
with our backend database respectively.

#### Parameters
`term` - String that contains the search term the user wishes to query.

### Endpoint Return
All API calls will return a JSON response type that contains each docket that has the keyword within it. <br>

* `200`<br>
```
{
  "data": {
    "search_term": "string",
    "documents": [
          {
            "author": "string",
            "date_posted": "date",
            "document_type": "string",
            "link": "string",
	    "docket_id": "string"
      }
    ]
  }
}
```
The response above will be returned for every API call with a 200 status code. All dockets relevant to the search will be formatted in a list. Within each docket object is relevant information such 
as the number of comments and the number of documents that are contained within the docket. A link for each search hit will be returned as well that leads the user to the relevant docket on 
regulations.gov. 

* 400
```
{
    "error": {
        "code": "integer",
        "message": "string"
    }
}
```
The response above will be returned for every API call with a 400 status code. If the caller does not provide a search term, the server will return a 400 error because the term was not found.


## /search_comments
### Description
The name for the API endpoint will be '/search_comments'. This endpoint will be used to search our database for comments within that contain the specified term and will return all comments that contain it.

### Calling the Endpoint
`/search_comments?term=SEARCH_PARAMETER&docket_id=IDNUMBER`<br>
To call the endpoint, hit the example API call above and replace the `term` query parameter with the term the caller wants to search for. The endoint will process the query parameter and interact with our backend database respectively.

#### Parameters
`term` - String that contains the search term the user wishes to query.
`docket_id` - Integer that contains the docket id the user wishes to query.

### Endpoint Return
All API calls will return a JSON response type that contains each docket that has the keyword within it. <br>

* `200`<br>
```
{
  "data": {
    "search_term": "string",
    "comments": [
      {
        "author": "string",
        "date_posted": "date",
        "link": "string",
        "docket_id": "string"
      }
    ]
  }
}
```
The response above will be returned for every API call with a 200 status code. All comments relevant to the search will be formatted in a list. Within each comment object is relevant information such as the author and the date posted that are contained within the docket. A link for each search hit will be returned as well that leads the user to the relevant comment on regulations.gov.

* 400
```
{
    "error": {
        "code": "integer",
        "message": "string"
    }
}
```
The response above will be returned for every API call with a 400 status code. If the caller does not provide a search term, the server will return a 400 error because the term was not found.
