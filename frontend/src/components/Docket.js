import React from "react";
import "../styles/Docket.css"; // Import the CSS file
import ZipButton from "./ZipButton";

const Docket = ({
 title,
 email,
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
   <article className="docket-container">
    <header className="docket-header">
     <h2 className="docket-title">{title}</h2>
     <p className="docket-agency">{docket_agency}</p>
    </header>
    <p className="docket-type">{docket_type}</p>
    <footer className="docket-footer">
     <a href={link} className="docket-link" target="_blank" rel="noopener noreferrer">
      Preview Docket {id} Here
     </a>
    </footer>
   </article>
   <div className="container-2">
    <div className="left-half">
     <p>
      {comments_containing} comments relate to your term out of the {total_comments} total comments
      in this docket.
     </p>
     <p>Comment Date Range: {comment_date_range}</p>
     <p>
      {documents_containing} documents relate to your term out of the {total_documents} total
      documents in this docket.
     </p>
    </div>
    <ZipButton email={email} docketID={id} />
   </div>
  </div>
 );
};

export default Docket;
