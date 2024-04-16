const header = document.getElementById("card")
const headerId = header.id
header.removeAttribute("id")
header.classList.add(headerId)

const img = document.querySelector(".card-img-top")
img.src = "book.png"
