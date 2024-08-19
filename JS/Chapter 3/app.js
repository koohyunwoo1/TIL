const h1 = document.querySelector("div.hello:first-child h1")
// // querySelector -> 오로지 첫번째것만 console에 띄워준다.
// // querySelectorAll -> 인자에 적합한 모든 것을 console에 출력해준다.

// title.innerText = "Hello";


// 글자를 클릭했을떄
// function handleTitleClick() {
//   h1.style.color = "blue";
//   console.log("title was clicked!");
// }

// h1.addEventListener("click", handleTitleClick);

// // 마우스가 글자에 다가왔을때
function handleMouseEnter() {
  h1.style.color = "red";
  h1.innerText = "Mouse is here!";
}

h1.addEventListener("mouseenter", handleMouseEnter);

// // // 마우스가 글자에서 나갔을때
function handleMouseLeave() {
  h1.style.color = "green";
  h1.innerText = "Mouse is gone!";
}

h1.addEventListener("mouseleave", handleMouseLeave);

// // 3.5
// //  resize


// function handleWindowResize() {
//   document.body.style.backgroundColor = "tomato";
// }

// function handleWindowCopy() {
//   alert("copier!")
// }


// function handleWindowOffline() {
//   alert("SOS no WIFI")
// }

// function handleWindowOnline() {
//   alert("ALL GOOD")
// }
// h1.addEventListener("click", handleTitleClick);
// h1.addEventListener("mouseenter", handleMouseEnter);
// h1.addEventListener("mouseleave", handleMouseLeave);


// window.addEventListener("resize", handleWindowResize);
// window.addEventListener("copy", handleWindowCopy);

// // 우리가 wifi에 연결되어있는지 ?
// window.addEventListener("offline", handleWindowOffline);
// window.addEventListener("online", handleWindowOnline);



// 3.6


// const h1 = document.querySelector("div.hello:first-child h1")


// h1.style.color가 blue이면 tomato로 변경해주세요


// style 같은 것은 css에서 하는것을 권장한다.

// function handleTitleClick() {
//   const currentColor = h1.style.color;
//   let newColor;
//   if(currentColor === "blue"){
//     newColor = "tomato";
//   } else {
//     newColor = "blue";
//   }
//   h1.style.color = newColor;
// }

// h1.addEventListener("click", handleTitleClick);


// 3.7

// css에서 스타일을 작성하고 함수만 js에서 하는 방식
// const h1 = document.querySelector("div.hello:first-child h1")

// function handleTitleClick() {

//   h1.classList.toggle("active");
// }

// h1.addEventListener("click", handleTitleClick);


// 3.8 html에서 class가 지정되어있는 상태에서 자바스크립트에서 어떻게 안 없애고
// class를 그대로 유지한 상태에서 표현 할 수 있을까 ?
// toggle은 h1의 classList에 activ e class가 이미 있는지 확인해서
// 만약 있다면, toggle이 active를 제거해준다.
// 만약 없다면, toggle은 active를 추가 해준다.

