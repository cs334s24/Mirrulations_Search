import React from 'react';
import SearchResult from './SearchResult'; // Assuming SearchResult.js is in the same directory

const SearchResultsList = ({dockets}) => {
  // Sample data for demonstration
  const staticDockets = [
    {
      title: "Sample Title 1",
      id: 1,
      link: "https://example.com/sample1",
      number_of_comments: 10,
      number_of_documents: 5
    },
    {
      title: "Sample Title 2",
      id: 2,
      link: "https://example.com/sample2",
      number_of_comments: 5,
      number_of_documents: 3
    }
  ];

  return (
    <div className="search-results-list">
      {dockets.map((docket, index) => (
        <SearchResult
          key={index}
          title={docket.title}
          id={docket.id}
          link={docket.link}
          number_of_comments={docket.number_of_comments}
          number_of_documents={docket.number_of_documents}
        />
      ))}
    </div>
  );
};

export default SearchResultsList;
