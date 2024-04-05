const URL = window.location.href;

// api.js
export const getDummyData = async (searchTerm) => {
 try {
  const search = `https://localhost/api/search_dockets?term=${searchTerm.replaceAll("/", "").replaceAll("'", "").replaceAll('"', "")}`;
  const response = await fetch(search);

  const data = await response.json();
  return data;
 } catch (error) {
  console.error("Error calling the endpoint:", error);
 }
};

export const getDummyDataDemo = async () => {
 try {
  const data = [
   {
    title: "Proposed Informaation Collestion: Final Rule to Implememnt Title V of the Tribal...",
    id: "IHS-2005-0001",
    //Add Agency Name
    link: "https://www.regulations.gov/docket/IHS-2005-0001",
    docket_type: "Notice",
    documents_containing: 54,
    total_documents: 54,
    date_range: "2008/3/13 - 2010/4/25",
    comment_date_range: "2008/3/13 - 2010/4/25",
    comments_containing: 20,
    total_comments: 100,
   },
  ];
  return data;
 } catch (error) {
  console.error("Error calling the endpoint:", error);
 }
};

// export default [getDummyData, getDummyDataDemo];
