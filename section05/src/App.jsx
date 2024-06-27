import './App.css'
import Header from './components/Header'
import Main from './components/Main'
import Footer from './components/Footer'
import Button from './components/Button'
// 확장자는 굳이 안써도됨.

// 부모 컴포넌트
function App() {

  return (
    <>  
      <Button text={"메일"} color={"red"}/>
      <Button text={"카페"}/>
      <Button text={"블로그"}/>
    </>
  )
}

export default App
