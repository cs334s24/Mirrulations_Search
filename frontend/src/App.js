import React, {useState} from "react";
import "./App.css";
// import {getDummyDataDemo} from "./static/script";
import {fetchDockets} from "./static/script";
import SearchBar from "./components/SearchBar";
import DocketList from "./components/DocketList";

function App() {
 const [dockets, setDockets] = useState(); // Initialize docket state to false
 const [email, setEmail] = useState();
 const handleOnClick = async (term) => {
  const data = await fetchDockets(term);
  setDockets(data.data.dockets);
 };

 const handleInputChange = async (event) => {
  setEmail(event.target.value);
 };

 return (
  <div className="App">
   <input
    type="text"
    value={email}
    onChange={handleInputChange}
    placeholder="Enter Email"
    className="search-input" // Add the search-input class
   />
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
