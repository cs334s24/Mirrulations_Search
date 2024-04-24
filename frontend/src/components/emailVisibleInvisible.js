import React from "react";

function EmailVisibleInvisible({isVisible, handleInputChange}) {
 return isVisible && <input type="email" onChange={handleInputChange} placeholder="Enter Email" />;
}

export default EmailVisibleInvisible;
