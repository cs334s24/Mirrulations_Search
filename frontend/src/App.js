import React from 'react';
import './App.css';
import callTestEndpoint from './static/script';
import SearchBar from './components/SearchBar';

const handleOnClick = async () => {
  const data = await callTestEndpoint()
  console.log(data)
  document.getElementById('responseContainer').innerHTML = data.message;
}

function App() {
  return (
    <div className="App">
      <body>
        <h1>Mirrulations Search</h1>
        <div>
          <SearchBar/>
        </div>
      </body>
    </div>
  );
}

export default App;
