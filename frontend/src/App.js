import React, {useState} from "react";
import "./App.css";
// import {getDummyDataDemo} from "./static/script";
import {getDummyData} from "./static/script";
import SearchBar from "./components/SearchBar";
import DocketList from "./components/DocketList";
import AppBackgroundHomepageImage from "./images/homepage pic.jpeg";
import AppBackgroundSearchResultsImage from "./images/grey background.jpeg";

function App() {
 const [dockets, setDockets] = useState(); // Initialize docket state to false
 const [currentImage, setCurrentImage] = useState(AppBackgroundHomepageImage); // Initialize currentImage and set it to AppBackgroundHomepageImage
 const handleOnClick = async (term) => {
  try {
   const data = await getDummyData(term);
   if (data.data.dockets.length === 0) {
    alert("No results found for: '" + term + "'");
   } else {
    setDockets(data.data.dockets);
    setCurrentImage(AppBackgroundSearchResultsImage);
    console.log("image should be changing now");
   }
  } catch (error) {
   console.log(error);
  }
 };

 return (
  <div className="App">
   <div className="App-background_homepageimage" style={{backgroundImage: `url(${currentImage})`}}>
    <h1>Mirrulations Search</h1>
    <div>
     <SearchBar handleOnClick={handleOnClick} />
     {dockets && <DocketList dockets={dockets} />}{" "}
     {/* Render SearchResultsList only if dockets is true */}
    </div>
   </div>
  </div>
 );
}

export default App;
