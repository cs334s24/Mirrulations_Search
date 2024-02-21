import React from 'react';
import '../styles/SearchResult.css'; // Import the CSS file

const SearchResult = ({ title, id, link, number_of_comments, number_of_documents }) => {
  return (
    <div className="search-result">
      <h2>Title: {title}</h2>
      <p>Link (ID): <a href={link}>{id}</a></p>
      <p>Number of Comments: {number_of_comments}</p>
      <p>Number of Documents: {number_of_documents}</p>
    </div>
  );
};

export default SearchResult;
