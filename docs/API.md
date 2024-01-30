# API Documentation

## /search
### Description
The name for the API endpoint will be `/search`. This endpoint will be used to search our database for dockets that contain the specified term and will return all dockets that contain it. Within the dockets, specific comments and documents that contain that term will also be specified. 

### Calling the Endpoint
`/search?terms=SEARCH_PARAMETERS`<br>
To call the endpoint, hit the example API call above and replace the `terms` query parameter with the terms the caller wants to search. The endoint will process the query parameter and interact with our backend database respectively.

#### Parameters
`terms` - String that contains all terms that the user wants to search for. Each term is separated by a single space.

### Endpoint Return
All API calls will return a JSON response type that contains each docket that has the keyword within it. <br>

* `200`<br>
```
{
  "data": {
    "dockets": [
      {
        "title": "string",
        "id": "integer",
        "link": "string",
        "comments": [
          {
            "author": "string",
            "date_posted": "date",
            "link": "string"
          }
        ],
        "documents": [
          {
            "author": "string",
            "date_posted": "date",
            "document_type": "string",
            "link": "string"
          }
        ]
      }
    ]
  }
}
```
The response above will be returned for every API call with a 200 status code. All dockets relevant to the search will be formatted in a list. Within each docket object is relevant information such as comments and documents that also contain the search terms. A link for each search hit will be returned as well that leads the user to the relevant comment on regulations.gov. 

* 400
```
{
    "error": {
        "code": "integer",
        "message": "string"
    }
}
```
The response above will be returned for every API call with a 400 status code. If the request does not exist and a 404 error is returned, the code will be 404 and the message will explain that the request is not a valid request to our server.
