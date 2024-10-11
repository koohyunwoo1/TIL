import "./App.css";
import Home from "../src/pages/Home/Home";
import Project from "../src/pages/Project/Project";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/project" element={<Project />} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
