function callEndpoint() {
    var fakeResponse = {
        message: "This isn't set up to the endpoint yet"
    };
    document.getElementById('responseContainer').innerText = 'Response: ' + JSON.stringify(fakeResponse);
}

