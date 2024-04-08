# Pagination Documentation

## What is Pagination

Pagination is a process of dividing data into discrete pages, allowing users to view a specific subset of data at a time. This will be useful when we switch to a large data set, as it will reduce the amount of data transferred at once and improve the response times.

## Pagination in MongoDB

MongoDB supports pagination through the skip() and limit() functions
* `limit(n)` limits the number of documents returned to n
* `skip(n)` skips the first n documents

## Implementing Pagination