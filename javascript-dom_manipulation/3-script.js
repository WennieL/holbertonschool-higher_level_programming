let header = document.querySelector("header");
let toggle_header = document.getElementById("toggle_header");

toggle_header.addEventListener("click", function() {
  header.classList.toggle("red");
  header.classList.toggle("green");
});