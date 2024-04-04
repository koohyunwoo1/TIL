const title = document.querySelector("div.hello:first-child h1")
// querySelector -> 오로지 첫번째것만 console에 띄워준다.
// querySelectorAll -> 인자에 적합한 모든 것을 console에 출력해준다.

// title.innerText = "Hello";

function handleTitleClick() {
  title.style.color = "blue"
  console.log("title was clicked!");
}

function handleMouseEnter() {
  title.style.color = "red"
  title.innerText = "Mouse is here!";
}

function handleMouseLeave() {
  title.style.color = "green"
  title.innerText = "Mouse is gone!";
}

// 웹 사이트에서 클릭 횟수를 인지하는 방법
title.onclick = handleTitleClick
title.onmouseenter = handleMouseEnter;
title.addEventListener("mouseleave", handleMouseLeave);

//  3. 5