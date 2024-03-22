const URL = window.location.href;

// api.js
export const getDummyData = async (searchTerm) => {
 try {
  const search = URL + "/api/search_dockets?term=" + searchTerm;
  const response = await fetch(search);

  const data = await response.json();
  console.log(data);
  return data;
 } catch (error) {
  console.error("Error calling the endpoint:", error);
 }
};

export const getDummyDataDemo = async () => {
    try{
        const data = [{
            title: "Tribal Self Gevernance", 
            id: "IHS-2008-1", 
            link: "http://localhost",
            docket_type: "Notice", 
            documents_containing: 54,
            total_documents: 54,
            date_range: "2008/3/13 - 2010/4/25",
            comment_date_range: "2008/3/13 - 2010/4/25",
            comments_containing:20,
            total_comments: 100
        }]
        return data;
    } catch (error) {
     console.error("Error calling the endpoint:", error);
    }
}

// export default [getDummyData, getDummyDataDemo];
