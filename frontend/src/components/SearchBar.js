import React, {useState} from "react";
import "../styles/SearchBar.css";

const SearchBar = ({handleOnClick, setPage, setDockets, setTerm}) => {
 const [query, setQuery] = useState("");

 const handleInputChange = (event) => {
  setQuery(event.target.value);
 };

 const handleSearch = () => {
  setTerm(query);
  handleOnClick(query);
 };

 const handleKeyDown = (event) => {
  if (event.key === "Enter") {
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
    placeholder="Enter Search Term"
    className="search-input" // Add the search-input class
   />
   <button onClick={handleSearch} className="search-button">
    Search
   </button>
  </div>
 );
};

export default SearchBar;
