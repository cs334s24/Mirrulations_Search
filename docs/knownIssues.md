# Known Issues

This file was created for documenting all known issues about the project

## API

### Search Efficiency
The `search_dockets` API endpoint is repsonsible for the initial search for our system. The more data that the machine has, the longer the query takes to finish. This issue is top of the priority list when merging the full dataset into our application. Without fixing this, the API will most likely timeout with the large dataset. Some solutions to help address this issue would be creating indices for our data in Mongo, reducing the number of queries needed to look through all 3 Mongo collections, and changing pagingation so that the entire query doesn't run for each page that is loaded. A combination of these three or possibly all three will be needed to increase the efficiency.
