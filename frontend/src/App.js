import React, {useState} from "react";
import "./App.css";
// import {getDummyDataDemo} from "./static/script";
import {getDummyData} from "./static/script";
import SearchBar from "./components/SearchBar";
import DocketList from "./components/DocketList";

function App() {
 const [dockets, setDockets] = useState(); // Initialize docket state to false

 const handleOnClick = async (term) => {
  try {
   // This will display a message if the search term is invalid or no results are found
   // It still has issues with some search terms such as ' ' (a single space)
   if (!term) {
    alert("Please enter a valid search term.");
    return;
   } else {
    const data = await getDummyData(term);
    if (data.data.dockets.length === 0) {
     alert("No results found for: '" + term + "'");
     return;
    } else {
     setDockets(data.data.dockets);
    }
   }
  } catch (error) {
   console.log(error);
  }
 };

 return (
  <div className="App">
   <h1>Mirrulations Search</h1>
   <div>
    <SearchBar handleOnClick={handleOnClick} />
    {/* list total number of dockets found for the term */}
    {dockets && <h2>{dockets.length} Results Found</h2>}
    {dockets && <DocketList dockets={dockets} />}{" "}
    {/* Render SearchResultsList only if dockets is true */}
   </div>
  </div>
 );
}

export default App;
