import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "./pages/Home";
import Game from "./pages/Game";
import Sidebar from "./components/SideBar";
import GameDrum from "./components/Drum/GameDrum";
import GameMelody from "./components/Melody/GameMelody";
import GamePiano from "./components/Piano/GamePiano";
import "./App.css";

const App = () => {
  return (
    <Router>
      <div className="app-container">
        <Sidebar />
        <div className="main-content">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/Game" element={<Game />} />
            <Route path="/drum" element={<GameDrum />} />
            <Route path="/melody" element={<GameMelody />} />
            <Route path="/piano" element={<GamePiano />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
};

export default App;
