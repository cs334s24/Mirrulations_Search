const express = require("express");
const path = require("path");

const app = express();
const port = process.env.PORT || 3000;

// Serve static files from the React app
app.use(express.static(path.join(__dirname, "my-react-app/build")));

// Define additional API routes or server logic as needed

// Handle React routing, return all requests to the React app
app.get("*", (req, res) => {
 res.sendFile(path.join(__dirname, "my-react-app/build", "index.html"));
});

app.listen(port, () => {
 console.log(`Server is running on port ${port}`);
});
