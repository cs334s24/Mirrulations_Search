import React, {useState} from "react";
import "../styles/SearchBar.css";

const SearchBar = ({handleOnClick}) => {
 const [query, setQuery] = useState("");

 const handleInputChange = (event) => {
  setQuery(event.target.value);
 };

 const handleSearch = () => {
  handleOnClick(query);
 };

 const handleKeyDown = (event) => {
  if (event.key === "Enter") {
   //    docker;
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
   <button onClick={handleSearch} className="search-button">
    Search
   </button>
  </div>
 );
};

export default SearchBar;
