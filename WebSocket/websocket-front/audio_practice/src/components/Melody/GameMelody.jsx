import { useState } from "react";
import useMelodyGame from "../../hooks/Melody/useMelodyGame";
import "../../style/Melody/GameMelody.css";
import Button from "../../components/Common/Button";

const GameMelody = () => {
  const [targetNote, setTargetNote] = useState("C4");
  const { message, currentNote, isGameActive, startGame } =
    useMelodyGame(targetNote);

  return (
    <div className="GameMelodyContainer">
      <div className="GameMelodyTitle">퍼펙트 싱어</div>
      <div className="Mission">미션: {targetNote} 음 맞추기</div>

      <div className="NoteDisplay">
        {currentNote ? `현재 음정: ${currentNote}` : "음성을 감지 중..."}
      </div>

      <div className="MelodyButtonContainer">
        <Button onClick={startGame}>
          {isGameActive ? "게임 끝" : "게임 시작"}
        </Button>
      </div>

      <div
        className={`MelodyMessageDisplay ${
          message === "Perfect!" ? "perfect" : ""
        }`}
      >
        {currentNote && message}
      </div>
    </div>
  );
};

export default GameMelody;
