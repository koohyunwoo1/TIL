const name = document.querySelector('#name')
// id가 name인 첫번째 요소를 선택 해서 name에 반환
// id여서 # 붙이기
// class면 .
const job = document.querySelector('#job')
const experience = document.querySelector('#experience')
const email = document.querySelector('#email')
const phone = document.querySelector('#phone')

name.textContent = '홍길동'
job.textContent = '의적'
experience.textContent = '서당'
email.textContent = 'hgd@korea'
phone.textContent = '010-1234-1234'

const img = document.querySelector('img')
img.setAttribute('src', 'profile.jpg') 
img.setAttribute('alt', '프로필 사진') 


// getElementById : 오직 ID를 사용하여 요소를 선택
// HTML 문서에서 유일한 ID를 가진 요소를 선택할 때 사용