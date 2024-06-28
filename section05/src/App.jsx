import './App.css'
import Header from './components/Header'
import Main from './components/Main'
import Footer from './components/Footer'
import Button from './components/Button'
// 확장자는 굳이 안써도됨.

// 부모 컴포넌트
function App() {
  const buttonPorps ={
    text : '메일',
    color : 'red',
    a : 1,
    b : 2,
    c : 3,
  }
  return (
    <>  
      <Button {...buttonPorps}/>
      <Button text={"카페"}/>
      <Button text={"블로그"}>
        <div>
          자식요소
        </div>
        <Header />
      </Button>
    </>
  )
}

export default App
