const URL = window.location.href;

// api.js
const getDummyData = async (searchTerm) => {
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

export default getDummyData;
