

// input이랑 button을 끌어오자

// const loginInput = document.querySelector("#login-form input");
// const loginButton = document.querySelector("#login-form button");

// function onLoginBtnClick() {
//   console.dir(loginInput.value);
//   // console.log("click !!!!");
// }

// loginButton.addEventListener("click", onLoginBtnClick);


// 이름을 입력했을때만 클릭이 가능하게

// const loginInput = document.querySelector("#login-form input");
// const loginButton = document.querySelector("#login-form button");

// function onLoginBtnClick() {
//   const username = loginInput.value;
//   console.log(username)
// }


// loginButton.addEventListener("click", onLoginBtnClick);


// 4.2



// 로그인 폼을 제출하더라도 페이지가 새로고침이 되지 않게 하기 위해 ?

// const loginInput = document.querySelector("#login-form input");
// const loginForm = document.querySelector("#login-form");

// const link = document.querySelector("a")

// function onLoginSubmit(event) {
//   event.preventDefault();
//   console.log(loginInput.value);
// }

// function handleLinkClick() {
//   alert("clicked !");
// }

// loginForm.addEventListener("submit", onLoginSubmit);
// link.addEventListener("click", handleLinkClick);





// 4. 3
// JS를 통해서 기본동작을 막아보자

// const loginForm = document.querySelector("#login-form");
// const loginInput = document.querySelector("#login-form input");

// const link = document.querySelector("a");

// function onLoginSubmit(event) {
//   event.preventDefault();
//   console.log(loginInput.value);
// }


// loginForm.addEventListener("submit", onLoginSubmit);


// 4. 4
// const loginForm = document.querySelector("#login-form");
// const loginInput = document.querySelector("#login-form input");
// const greeting = document.querySelector("#greeting");

// const HIDDEN_CLASSNAME = "hidden";

// function onLoginSubmit(event) {
//   event.preventDefault();
//   // 기본동작이 실행되지 않도록 막아주고
//   loginForm.classList.add(HIDDEN_CLASSNAME)
//   // hidden이라는 class name을 더해줘서 form을 숨기고
//   const username = loginInput.value;
//   // 유저의 이름을 변수로 저장해주고, 그 이름은 h1 안에 넣어준다.

//   // 2가지의 방법이 있다.
//   // 후자가 좀 더 좋아 보이네 ?
//   // greeting.innerText = "Hello " + username;
//   greeting.innerText = `Hello ${username}`;

//   // string을 넣고 싶다면 ${변수명} 하면 끝이다.
//   // ``백틱 기호로 시작하고 끝내야 한다.
//   greeting.classList.remove(HIDDEN_CLASSNAME)

// }


// loginForm.addEventListener("submit", onLoginSubmit);



// 4. 5
// Saving Username

// const loginForm = document.querySelector("#login-form");
// const loginInput = document.querySelector("#login-form input");
// const greeting = document.querySelector("#greeting");
// const HIDDEN_CLASSNAME = "hidden";



// function onLoginSubmit(event) {
//   event.preventDefault();
//   loginForm.classList.add(HIDDEN_CLASSNAME)
//   const username = loginInput.value;
//   localStorage.setItem("username", username)
//   // setItem을 사용하면 local storage에 정보를 저장할 수 있다.
  
//   greeting.innerText = `Hello ${username}`;
//   // greeting id에 Hello ~ 추가해준다.
//   greeting.classList.remove(HIDDEN_CLASSNAME)
// }


// loginForm.addEventListener("submit", onLoginSubmit);


// 4. 6
// local storage가 비어 있으면 form부터 보여주면서 지금까지 해오던 걸 하면 된다.
// local storage에 유저 정보가 있으면 form을 보여주면 안된다.
// h1 요소를 보여줘야 한다.

const loginForm = document.querySelector("#login-form");
const loginInput = document.querySelector("#login-form input");
const greeting = document.querySelector("#greeting");
const HIDDEN_CLASSNAME = "hidden";
const USERNAME_KEY = "username";


function onLoginSubmit(event) {
  event.preventDefault();
  loginForm.classList.add(HIDDEN_CLASSNAME)
  const username = loginInput.value;
  localStorage.setItem(USERNAME_KEY, username)
  paintGreeting(username);

}

function paintGreeting(username){
  greeting.innerText = `Hello ${username}`;
  greeting.classList.remove(HIDDEN_CLASSNAME);
}

loginForm.addEventListener("submit", onLoginSubmit);


const savedUsername = localStorage.getItem(USERNAME_KEY);

if (savedUsername === null) {
  // show the form
  loginForm.classList.remove(HIDDEN_CLASSNAME);
  loginForm.addEventListener("submit", onLoginSubmit);
} else {
  // show the greeting
    paintGreeting(savedUsername)
}


// 4.7
// 복습



