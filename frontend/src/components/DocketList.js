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
        docket_type={docket.docket_type}
        documents_containing={docket.documents_containing}
        total_documents={docket.total_documents}
        date_range={docket.date_range}
        comments_containing={docket.comments_containing}
        total_comments={docket.total_comments}
    />
   ))}
  </div>
 );
};

export default SearchResultsList;
