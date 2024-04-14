import React from "react";
import "../styles/Homepage_image.css"; // Import the CSS file
import backgroundImage from "../images/backgroundImage.jpg";
import SearchBar from "./SearchBar";
import DocketList from "./DocketList";

function App() {
    return (
      <div style={{
        backgroundImage: `url(${backgroundImage})`,
        backgroundPosition: 'center',
        backgroundSize: 'cover',
        backgroundRepeat: 'no-repeat'
      }}>
        {/* Your other components go here */}
      </div>
    );
  }
  
  export default App;
