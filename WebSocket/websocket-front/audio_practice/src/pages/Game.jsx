import Chat from "../components/chat";
import "../style/Game.css";
import { Link } from "react-router-dom";
import { FaDrum, FaGuitar, FaMicrophone } from "react-icons/fa";
import { GiPianoKeys } from "react-icons/gi";

const Game = () => {
  return (
    <div className="GameContainer">
      <div className="GameTitle">게임 페이지</div>
      <div className="CategoryContainer">
        <Link to="/drum" className="GameCategory">
          <FaDrum className="CategoryIcon" />
          <span>드럼</span>
        </Link>
        <Link to="/piano" className="GameCategory">
          <GiPianoKeys className="CategoryIcon" /> <span>건반</span>
        </Link>
        <Link to="/melody" className="GameCategory">
          <FaMicrophone className="CategoryIcon" />
          <span>보컬</span>
        </Link>
        <Link to="/guitar" className="GameCategory">
          <FaGuitar className="CategoryIcon" />
          <span>기타</span>
        </Link>
      </div>
      <div>
        <Chat />
      </div>
    </div>
  );
};

export default Game;
