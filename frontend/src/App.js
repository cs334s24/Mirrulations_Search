import React, {useState} from "react";
import "./App.css";
// import {getDummyDataDemo} from "./static/script";
import {getDummyData} from "./static/script";
import SearchBar from "./components/SearchBar";
import DocketList from "./components/DocketList";

function App() {
 const [dockets, setDockets] = useState(); // Initialize docket state to false

 const handleOnClick = async () => {
  const data = await getDummyData("Hi");
  console.log(data.data.dockets);
  setDockets(data.data.dockets);
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
