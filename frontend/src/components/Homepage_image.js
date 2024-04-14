import React from "react";
import "../styles/Homepage_image.css"; // Import the CSS file
import SearchBar from "./SearchBar";
import "../styles/SearchBar.css";
import Button from "./Button";
import "../styles/Button.css";
import images from "/Users/annahuang/Desktop/Capstone/Mirrulations_1Search/frontend/src/images/homepage pic.jpeg";


const Homepage_image = () => {
  return (
    <div className="Homepage_image">
    <img src={images} alt="this will be the homepage background picture" />
    <div className="search-bar">
      <SearchBar />
      <Button />
    </div>
    </div>
  );
};
export default Homepage_image;