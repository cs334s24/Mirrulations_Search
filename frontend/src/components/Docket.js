import React from "react";
import "../styles/Docket.css"; // Import the CSS file

const Docket = ({title, id, link,docket_type, documents_containing,total_documents,date_range,comments_containing,total_comments}) => {
 return (
  <div className="search-result">
   <h2>Title: {title}</h2>
   <p>
    Link (ID): <a href={link}>{id}</a>
   </p>
   <p>Number of Comments: {comments_containing}/{total_comments}</p>
   <p>Number of Documents: {documents_containing}/{total_documents}</p>
   <p>Date Range: {date_range}</p>
    <p>Comment Date Range: {comment_date_range}</p>
    <p>Docket Type:{docket_type}</p>
  </div>
 );
};

export default Docket;
