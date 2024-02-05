# API Documentation

## /search_dockets
### Description
The name for the API endpoint will be `/search_dockets`. This endpoint will be used to search our database for dockets that contain the specified term and will return all dockets that contain it. Within the dockets, specific comments and documents that contain that term will also be specified. 

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
    "search_term": "string",
    "dockets": [
      {
        "title": "string",
        "id": "integer",
        "link": "string",
        "number_of_comments": "int",
        "number_of_documents": "int"
      }
    ]
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

## /search_comments
