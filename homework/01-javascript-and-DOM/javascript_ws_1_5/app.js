const oldArticle = document.querySelector("article.card")

const newArticle = document.createElement("article")
newArticle.className = "card"
newArticle.style.width = "18rem"

const newDiv = document.createElement("div")
newDiv.className = "card-body"

const newH5 = document.createElement("h5")
newH5.className = "card-title"
newH5.textContent = "카드 제목"

const newP = document.createElement("p")
newP.className = "card-text"
newP.textContent = "카드 내용"

newDiv.appendChild(newH5)
newDiv.appendChild(newP)

newArticle.appendChild(newDiv)

const section = document.querySelector("section")
section.appendChild(newArticle)

oldArticle.parentNode.removeChild(oldArticle)

