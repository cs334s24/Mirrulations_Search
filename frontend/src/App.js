import React, {useState} from "react";
import "./App.css";
// import {getDummyDataDemo} from "./static/script";
import {fetchDockets} from "./static/script";
import SearchBar from "./components/SearchBar";
import DocketList from "./components/DocketList";
import EmailVisibleInvisible from "./components/emailVisibleInvisible";

function App() {
 const [dockets, setDockets] = useState(); // Initialize docket state to false
 const [email, setEmail] = useState();
 const [validTerm, setValidTerm] = useState(false);

 const handleOnClick = async (term) => {
  try {
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
     setValidTerm(true);
    }
   }
  } catch (error) {
   console.log(error);
  }
 };

 const handleInputChange = async (event) => {
  setEmail(event.target.value);
 };

 return (
  <div className="App">
   {/* <input
    type="text"
    value={email}
    onChange={handleInputChange}
    placeholder="Enter Email"
    className="search-input" // Add the search-input class
   /> */}
   <h1>Mirrulations Search</h1>
   <div>
    <SearchBar handleOnClick={handleOnClick} />
    <EmailVisibleInvisible isVisible={validTerm} handleInputChange={handleInputChange} />
    {/* list total number of dockets found for the term */}
    {dockets && <h2>{dockets.length} Results Found</h2>}
    {dockets && <DocketList dockets={dockets} />}{" "}
    {/* Render SearchResultsList only if dockets is true */}
   </div>
  </div>
 );
}

export default App;
