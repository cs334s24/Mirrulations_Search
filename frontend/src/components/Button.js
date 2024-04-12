import React, {useState} from "react";
import "../styles/Button.css";
import {zipFiles} from "../static/script";

const Button = () => {
 const handleClick = async () => {
  zipFiles();
 };

 return (
  <div>
   <button onClick={handleClick}>Download</button>
  </div>
 );
};

export default Button;
