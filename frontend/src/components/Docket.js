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
   <div className="header">
    <div className="h-row1">
     <div className="h-col1">
      <p>
       {docket_agency} - {docket_type} -{" "}
       <a href={link} target="_blank" rel="noopener noreferrer">
        {id}
       </a>
      </p>
     </div>
     <div className="h-col2">
      <Button id={id} />
     </div>
    </div>
    <div className="h-row2">
     <p>{title}</p>
    </div>
   </div>
   <div className="body">
    <div className="b-col1">
     <p>
      {documents_containing === 1 && total_documents === 1
       ? `1 document relates to your term out of the 1 document in this docket.`
       : documents_containing === 1
         ? `${documents_containing} document relates to your term out of the ${total_documents} total documents in this docket.`
         : total_documents === 1
           ? `${documents_containing} documents relate to your term out of the 1 document in this docket.`
           : `${documents_containing} documents relate to your term out of the ${total_documents} total documents in this docket.`}
     </p>
    </div>
    <div className="b-col2">
     <p>
      {comments_containing == 1 && total_comments === 1
       ? `1 comment relates to your term out of the 1 comment in this docket.`
       : comments_containing === 1
         ? `${comments_containing} comment relates to your term out of the ${total_comments} total comments in this docket.`
         : total_comments === 1
           ? `${comments_containing} comments relate to your term out of the 1 comment in this docket.`
           : `${comments_containing} comments relate to your term out of the ${total_comments} total comments in this docket.`}
     </p>
    </div>
    <div className="b-col3">
     <p>Comment Date Range: {comment_date_range}</p>
    </div>
   </div>
  </div>
 );
};

export default Docket;
