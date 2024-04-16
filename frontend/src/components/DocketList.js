import React from "react";
import Docket from "./Docket"; // Assuming SearchResult.js is in the same directory

const DocketList = ({dockets, email}) => {
 // Sample data for demonstration

 return (
  <div className="search-results-list">
   {dockets.map((docket, index) => (
    <Docket
     key={index}
     email={email}
     title={docket.title}
     id={docket.id}
     link={docket.link}
     docket_type={docket.docket_type}
     docket_agency={docket.docket_agency}
     documents_containing={docket.documents_containing}
     total_documents={docket.total_documents}
     comments_containing={docket.comments_containing}
     total_comments={docket.total_comments}
     comment_date_range={docket.comment_date_range}
    />
   ))}
  </div>
 );
};

export default DocketList;
