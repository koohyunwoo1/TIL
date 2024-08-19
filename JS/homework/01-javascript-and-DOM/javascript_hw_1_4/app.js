const name = document.querySelector('#name')
const job = document.querySelector('#job')
const experience = document.querySelector('#experience')
const email = document.querySelector('#email')
const phone = document.querySelector('#phone')
const sns = document.querySelector('#SNS')

name.textContent = '홍길동'
job.textContent = '의적'
experience.textContent = '서당'
email.textContent = 'hgd@korea'
phone.textContent = '010-1234-1234'
sns.textContent = 'hgd@sns.com'

const img = document.querySelector('img')
img.setAttribute('src', 'profile.jpg') 
img.setAttribute('alt', '프로필 사진') 

name.classList.add('highlight')
job.classList.add('highlight')
experience.classList.add('highlight')
email.classList.add('highlight')
phone.classList.add('highlight')
sns.classList.add('highlight')

const body = document.querySelector('body')
body.classList.add('container')

const title = document.querySelector('h1')
title.classList.add('title')

const imgTag = document.querySelector('img')
imgTag.classList.add('img')

