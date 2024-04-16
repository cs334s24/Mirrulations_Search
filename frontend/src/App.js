import React, {useState} from "react";
import "./App.css";
// import {getDummyDataDemo} from "./static/script";
import {fetchDockets} from "./static/script";
import SearchBar from "./components/SearchBar";
import DocketList from "./components/DocketList";

function App() {
 const [dockets, setDockets] = useState(); // Initialize docket state to false

 const handleOnClick = async (term) => {
  try {
   const data = await fetchDockets(term);
   setDockets(data.data.dockets);
  } catch (error) {
   // show a message to the user that there was an error
   alert("There was an error fetching the data. Please try again.");
   console.log(error);
  }
 };

 return (
  <div className="App">
   <h1>Mirrulations Search</h1>
   <div>
    <SearchBar handleOnClick={handleOnClick} />
    {dockets && <DocketList dockets={dockets} />}{" "}
    {/* Render SearchResultsList only if dockets is true */}
   </div>
  </div>
 );
}
export default App;
