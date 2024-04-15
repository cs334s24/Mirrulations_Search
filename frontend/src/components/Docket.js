import React from "react";
import "../styles/Docket.css"; // Import the CSS file
import Button from "./Button";

const Docket = ({
 title,
 id,
 link,
 docket_type,
 docket_agency,
 documents_containing,
 total_documents,
 comment_date_range,
 comments_containing,
 total_comments,
}) => {
 return (
  <div className="search-result">
   <div className="container-1">
    <p>{docket_agency}</p>
    <h2>{title}</h2>
    <p>{docket_type}</p>
    <p>
     <a href={link} target="_blank" rel="noopener noreferrer">
      {id}
     </a>
    </p>
   </div>
   <div className="container-2">
    <div className="left-half">
     <p>
      Related Comments: {comments_containing}/{total_comments}
     </p>
     <p>Comment Date Range: {comment_date_range}</p>
     <p>
      Related Documents: {documents_containing}/{total_documents}
     </p>
    </div>
    <Button />
   </div>
  </div>
 );
};

export default Docket;
