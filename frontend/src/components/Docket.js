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
   <article className="docket-container">
    <header className="docket-header">
     <p className="docket-agency">{docket_agency}</p>
     <h2 className="docket-title">{title}</h2>
    </header>
    <p className="docket-type">{docket_type}</p>
    <footer className="docket-footer">
     <a href={link} className="docket-link" target="_blank" rel="noopener noreferrer">
      Docket ID : {id}
     </a>
    </footer>
   </article>

   {/* <div className="container-1">
                <p>{docket_agency}</p>
                <h2>{title}</h2>
                <p>{docket_type}</p>
                <p>
                    <a href={link} target="_blank" rel="noopener noreferrer">
                        {id}
                    </a>
                </p>
            </div> */}
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
    <Button />
   </div>
  </div>
 );
};

export default Docket;
