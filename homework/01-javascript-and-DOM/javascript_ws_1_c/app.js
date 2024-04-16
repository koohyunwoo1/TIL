let divTag = document.createElement("div")
divTag.className = "article"

let h1Tag = document.createElement("h1")
h1Tag.textContent = "Article Title"

let pTag = document.createElement("p")
pTag.style.borderTop = "1px solid black"
pTag.style.paddingTop = "10px"
pTag.textContent = "This is an article content"

divTag.appendChild(h1Tag)
divTag.appendChild(pTag)
document.body.appendChild(divTag)
