import { useState } from "react";
import { FaDrum, FaMicrophone } from "react-icons/fa";
import { GiPianoKeys } from "react-icons/gi";
import Chat from "../components/chat";
import "../style/Game.css";
import GameDescriptionModal from "../components/GameDescription";

const Game = () => {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [selectedGame, setSelectedGame] = useState(null);

  const openModal = (game) => {
    setSelectedGame(game);
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false);
    setSelectedGame(null);
  };

  return (
    <div className="GameContainer">
      <div className="GameTitle">미니 게임</div>
      <div className="CategoryContainer">
        <button onClick={() => openModal("piano")} className="GameCategory">
          <GiPianoKeys className="CategoryIcon" /> <span>코드 천재</span>
        </button>
        <button onClick={() => openModal("drum")} className="GameCategory">
          <FaDrum className="CategoryIcon" />
          <span>리듬 킹</span>
        </button>
        <button onClick={() => openModal("melody")} className="GameCategory">
          <FaMicrophone className="CategoryIcon" />
          <span>퍼펙트 싱어</span>
        </button>
      </div>
      <div>
        <Chat />
      </div>
      <GameDescriptionModal
        isOpen={isModalOpen}
        onClose={closeModal}
        selectedGame={selectedGame}
      />
    </div>
  );
};

export default Game;
