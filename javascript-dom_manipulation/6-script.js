let character = document.getElementById("character");

fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
  .then((response) => {
    if(!response.ok) {
      throw new Error(`HTTP error: ${response.status}`);
    }
    return response.json();
  })
  .then((json) => {
    character.textContent = json.name;
  })
  .catch((error) => console.error(`Fetch problem: ${error.message}`));
