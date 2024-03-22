import React from "react";
import SearchResult from "./SearchResult"; // Assuming SearchResult.js is in the same directory

const SearchResultsList = ({dockets}) => {
 // Sample data for demonstration

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
