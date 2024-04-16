import React, {useState} from "react";
import "../styles/Button.css";
import {zipFiles} from "../static/script";

const Button = ({email, docketID}) => {
 const handleClick = () => {
  zipFiles(email, docketID);
 };

 return (
  <div>
   <button onClick={handleClick}>Download</button>
  </div>
 );
};

export default Button;
