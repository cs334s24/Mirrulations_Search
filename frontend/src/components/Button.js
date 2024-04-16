import React, {useState} from "react";
import "../styles/Button.css";

const Button = ({email, docketID}) => {
 const [clicked, setClicked] = useState(false);

 const handleClick = () => {
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
