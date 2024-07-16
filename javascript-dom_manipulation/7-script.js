let list_movies = document.getElementById("list_movies");

fetch("https://swapi-api.hbtn.io/api/films/?format=json")
  .then((response) => {
    if(!response.ok) {
      throw new Error(`HTTP error: ${response.status}`);
    }
    return response.json();
  })
  .then((json) => {
    const movies = json.results;
    for (let movie of movies) {
      let li = document.createElement("li");
      li.textContent = movie.title;
      list_movies.appendChild(li);
    }
  })
  .catch((error) => {
    console.error(`Fetch problem: ${error.message}`);
  })