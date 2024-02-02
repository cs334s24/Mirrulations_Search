function callEndpoint() {
    // Make a GET request to the /data endpoint
    fetch('/data')
        .then(response => response.json())
        .then(data => {
            // Display the message in the responseContainer
            document.getElementById('responseContainer').innerHTML = `<p>${data.message}</p>`;
        })
        .catch(error => {
            console.error('Error fetching data:', error);
            // Handle errors if needed
        });
}


// api.js
const callTestEndpoint = async () => {
    try {
      console.log("Script: ")
      const response = await fetch('http://localhost:8000/data'); // replace with your actual API endpoint
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error calling the endpoint:', error);
    }
  };
  
  export default callTestEndpoint;
  
