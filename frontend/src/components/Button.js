import React, {useState} from "react";
import "../styles/Button.css";
import {zipFiles} from "../static/script";

const Button = () => {
 const [clicked, setClicked] = useState(false);

 const handleClick = () => {
  alert(`An email containing a downloadable version of the docket has been sent`);
  setClicked(true);
  zipFiles();
 };

 const loadOtherDocket = () => {
  window.location.reload();
  setClicked(true);
 };

 return (
  <div>
   <button
    style={{background: !clicked ? "green" : "gray"}}
    onClick={
     !clicked
      ? () => {
         handleClick();
        }
      : null
    }
    disabled={clicked}>
    {!clicked ? "Download" : "Downloaded"}
   </button>
   <button className="load-docket-button" onClick={loadOtherDocket}>
    Load Other Docket
   </button>
  </div>
 );
};

export default Button;
