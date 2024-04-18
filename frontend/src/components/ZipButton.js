import React, {useState} from "react";
import "../styles/ZipButton.css";
import {zipFiles} from "../static/script";

const ZipButton = ({email, docketID}) => {
 const handleClick = () => {
  alert(
   `An email containing a downloadable version of docket ${docketID} has been sent to ${email}`,
  );
  zipFiles(email, docketID);
 };

 return (
  <div>
   <button onClick={handleClick}>Download</button>
  </div>
 );
};

export default ZipButton;
