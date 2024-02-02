import React from 'react';
import './App.css';
import callTestEndpoint from './static/script';

const handleOnClick = async () => {
  const data = await callTestEndpoint()
  console.log(data)
  document.getElementById('responseContainer').innerHTML = data.message;
}

function App() {
  return (
    <div className="App">
      <body>
        <h1>Kickoff Webapp</h1>
        <div>
          <button id="callEndpointButton" onClick={handleOnClick}>Click Me</button>
          <div id="responseContainer"></div>
        </div>
      </body>
    </div>
  );
}

export default App;
