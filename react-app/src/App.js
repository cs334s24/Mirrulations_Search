import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <body>
        <h1>Kickoff Webapp</h1>
        <div>
          <button id="callEndpointButton" onclick="callEndpoint()">Click Me</button>

          <div id="responseContainer"></div>
        </div>

        <script src="/static/script.js"></script>
      </body>
    </div>
  );
}

export default App;
