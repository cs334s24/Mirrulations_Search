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
const getDummyData = async (searchTerm) => {
    try {
      const response = await fetch(`http://localhost:8000/search_dockets?term=${searchTerm}`)
      
      const data = await response.json();
      console.log(data)
      return data;
    } catch (error) {
      console.error('Error calling the endpoint:', error);
    }
  };
  
  export default getDummyData;
  
