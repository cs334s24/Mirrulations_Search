const URL = window.location.href;

// api.js
export const fetchDockets = async (searchTerm) => {
 try {
  const search =
   URL +
   `api/search_dockets?term=${searchTerm.replaceAll("/", "").replaceAll("'", "").replaceAll('"', "")}`;
  const response = await fetch(search);

  const data = await response.json();
  return data;
 } catch (error) {
  console.error("Error calling the endpoint:", error);
 }
};

export const zipFiles = async (email, docketID) => {
 try {
  const search = URL + `api/zip_data`;
  const response = await fetch(search);
  const data = await response.json();
  return data;
 } catch (error) {
  console.error("Error calling the endpoint:", error);
 }
};
