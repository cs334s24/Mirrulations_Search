import React from "react";
import "../styles/pictures.css"; // Import the CSS file
import SearchBar from "./SearchBar";
import "../styles/SearchBar.css";
import Button from "./Button";
import "../styles/Button.css";
import images from "./images/homepage pic.jpeg";

const Homepage_image = () => {
 return (
  <div className="Homepage_image">
   <div className="search-bar">
    <SearchBar />
    <Button />
   </div>
  </div>
 );
};
export default Homepage_image;
