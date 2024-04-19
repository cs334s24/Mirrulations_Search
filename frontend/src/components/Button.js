import React, {useState} from "react";
import "../styles/Button.css";

const Button = () => {
 const [clicked, setClicked] = useState(false);

 const handleClick = () => {
  alert(`An email containing a downloadable version of docket has been sent`);
  setClicked(true);
 };

 return (
  <div>
   <button onClick={handleClick}>Download</button>
   {clicked && <p>Clicked</p>}
  </div>
 );
};

export default Button;
