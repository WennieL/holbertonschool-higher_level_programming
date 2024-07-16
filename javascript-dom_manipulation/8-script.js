document.addEventListener("DOMContentLoaded", () => {
  let hello = document.getElementById("hello");

  fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
    .then((response) => {
      if(!response.ok) {
        throw new Error(`HTTP error: ${response.status}`);
      }
      return response.json();
    })
    .then((json) => {
      hello.textContent = json.hello;
    })
    .catch((error) => console.error(`Fetch problem: ${error.message}`));
});
