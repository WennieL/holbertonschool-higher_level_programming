
const add_item = document.getElementById("add_item");
const my_list = document.querySelector(".my_list");

add_item.addEventListener("click", function() {
  const li = document.createElement("li");
  li.appendChild(document.createTextNode("Item"));
  my_list.appendChild(li);  
})