import React, {useState} from "react";
import "./App.css";
// import {getDummyDataDemo} from "./static/script";
import {fetchDockets} from "./static/script";
import SearchBar from "./components/SearchBar";
import DocketList from "./components/DocketList";

function App() {
 const [dockets, setDockets] = useState(); // Initialize docket state to false
 const [email, setEmail] = useState(""); // Initialize docket state to false

 const handleOnClick = async (term) => {
  try {
   const data = await fetchDockets(term);
   setDockets(data.data.dockets);
  } catch (error) {
   // show a message to the user that there was an error
   alert("There was an error fetching the data. Please try again.");
   // This will display a message if the search term is invalid or no results are found
   // It still has issues with some search terms such as ' ' (a single space)
   if (!term) {
    alert("Please enter a valid search term.");
    return;
   } else {
    const data = await fetchDockets(term);
    if (data.data.dockets.length === 0) {
     alert("No results found for: '" + term + "'");
     return;
    } else {
     setDockets(data.data.dockets);
    }
   }
  }
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
    {/* list total number of dockets found for the term */}
    {dockets && <h2>{dockets.length} Results Found</h2>}
    {dockets && <DocketList dockets={dockets} email={email} />}{" "}
    {/* Render SearchResultsList only if dockets is true */}
   </div>
  </div>
 );
}
export default App;
