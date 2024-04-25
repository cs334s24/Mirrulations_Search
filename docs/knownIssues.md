# Known Issues

This file was created for documenting all known issues about the project

## API

### Search Efficiency
The `search_dockets` API endpoint is repsonsible for the initial search for our system. The more data that the machine has, the longer the query takes to finish. This issue is top of the priority list when merging the full dataset into our application. Without fixing this, the API will most likely timeout with the large dataset. Some solutions to help address this issue would be creating indices for our data in Mongo, reducing the number of queries needed to look through all 3 Mongo collections, and changing pagingation so that the entire query doesn't run for each page that is loaded. A combination of these three or possibly all three will be needed to increase the efficiency.

## Frontend

### Linting/Prettier Errors
When making changes on anything in the Frontend folder theres a good chance that when trying to test the webpage you will get a linting error. This is because the linter wants the code to look a specifc way, so just because you get a linting error or "prettier" error it does not mean that what you wrote was wrong. You're gonna want to run these lines in your terminal everytime before you test your frontend changes so that your code gets reformated into the way the linter deems neccessary:

  ```
  cd frontend
  npx eslint --fix .
  ```