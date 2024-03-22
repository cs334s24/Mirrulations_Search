import React from "react";
import "../styles/Docket.css"; // Import the CSS file

const Docket = ({title, id, link,docket_type, documents_containing,total_documents,date_range, comment_date_range,comments_containing,total_comments}) => {
 return (
  <div className="search-result">
   <h2>{title}</h2>
   <p>{docket_type}</p>
   <p>
    <a href={link}>{id}</a>
   </p>
   <p>{date_range}</p>
   <p>Related of Comments: {comments_containing}/{total_comments}</p>
    <p2>Comment Date Range: {comment_date_range}</p2>
   <p>Related of Documents: {documents_containing}/{total_documents}</p>
  
  </div>
 );
};

export default Docket;
