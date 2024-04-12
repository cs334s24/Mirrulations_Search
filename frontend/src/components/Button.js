import React, {useState} from "react";
import "../styles/Button.css";

const Button = ({docket}) => {
 const [clicked, setClicked] = useState(false);

 const handleClick = () => {
  console.log(docket);
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
