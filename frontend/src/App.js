import React, { useState } from 'react';
import './App.css';
import getDummyData from './static/script';
import SearchBar from './components/SearchBar';
import SearchResultsList from './components/SearchResultList';

function App() {
  const [dockets, setDockets] = useState(); // Initialize docket state to false

  const handleOnClick = async () => {
    console.log("Hello");
    const data = await getDummyData();
    console.log(data.data.dockets);
    setDockets(data.data.dockets); // Set docket state to true when search button is clicked
  };

  return (
    <div className="App">
      <h1>Mirrulations Search</h1>
      <div>
        <SearchBar handleOnClick={handleOnClick}/>
        {dockets && <SearchResultsList dockets={dockets} />} {/* Render SearchResultsList only if dockets is true */}
      </div>
    </div>
  );
}

export default App;
