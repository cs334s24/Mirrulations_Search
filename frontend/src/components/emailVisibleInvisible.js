import React from "react";

// The email bar will only render an input field if the isVisible prop is true
// Makes sure the email bar is only visible after a valid search term is entered
function EmailVisibleInvisible({isVisible, handleInputChange}) {
 return isVisible && <input type="email" onChange={handleInputChange} placeholder="Enter Email" />;
}

export default EmailVisibleInvisible;
