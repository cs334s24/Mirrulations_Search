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

