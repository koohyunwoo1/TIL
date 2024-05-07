let count1 = 0
let count2 = 0

const scissorsBtn = document.querySelector('#scissors-button')
const rockBtn = document.querySelector('#rock-button')
const paperBtn = document.querySelector('#paper-button')


function playGame(player1, player2) { 
  if (player1 === 'scissors') {
    if (plyaer2 === 'rock') {
      count2 += 1
      return 2
    } else if (player === 'paper') {
      count1 += 1
      return 1
    } 
  } else if (player1 === 'rock') {
    if (player2 === 'scissors') {
      count1 += 1
      return 1
    } else  if (player === 'paper') {
      count2 += 1
      return 2
    }
  } else if (player1 === 'paper') {
    if (player2 === 'rock') {
      count1 += 1
      return 1
    } else if (player === 'scissors') {
      count2 += 1
      return 2
    }
  } else {
    return 0
  }

}


function buttonClickHandler(choice) {
  rockBtn.disabled = true
  scissorsBtn.disabled = true
  paperBtn.disabled = true

  constarr = ['rock', 'scissors','paper']

  const randomIndex = Math.floor(Math.random() * 3)



}