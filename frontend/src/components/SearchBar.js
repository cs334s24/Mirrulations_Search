import React, { useState } from 'react';
import '../styles/SearchBar.css';

const SearchBar = ({ onSearch, handleOnClick }) => {
  const [query, setQuery] = useState('');

  const handleInputChange = (event) => {
    setQuery(event.target.value);
  };

  const handleSearch = () => {
    // onSearch(query);
  };

  const handleKeyDown = (event) => {
    if (event.key === 'Enter') {
      handleSearch();
    }
  };

  return (
    <div className="search-bar">
      <input
        type="text"
        value={query}
        onChange={handleInputChange}
        onKeyDown={handleKeyDown}
        placeholder="Search..."
        className="search-input" // Add the search-input class
      />
      <button onClick={handleOnClick} className="search-button">Search</button>
    </div>
  );
};

export default SearchBar;
