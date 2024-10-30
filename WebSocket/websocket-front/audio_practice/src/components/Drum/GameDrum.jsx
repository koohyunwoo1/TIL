import useDrumGame from "../../hooks/Drum/useDrumGame";
import sounds from "../../utils/drumSound";
import CommonButton from "../Common/Button";
import "../../style/Drum/GameDrum.css";

const GameDrum = () => {
  const {
    currentBeat,
    score,
    pattern,
    isPlayingPattern,
    message,
    level,
    gameOver,
    isGameStarted,
    handleDrumClick,
    startPatternGame,
    resetGame,
    playPattern,
  } = useDrumGame();

  return (
    <div className="GameDrumContainer">
      <div className="GameDrumTitle">리듬 킹</div>
      {isGameStarted && (
        <>
          <div className="ScoreLevelContainer">
            점수 : {score} &nbsp; 단계: {level}
          </div>
          <div className="DrumMessageDisplay">{message}</div>
        </>
      )}
      <div className="DrumContainer">
        <div className="DrumRow">
          {Object.keys(sounds)
            .slice(0, 4)
            .map((beat) => (
              <div
                key={beat}
                className={`Drum ${currentBeat === beat ? "active" : ""} ${
                  isPlayingPattern ? "disabled" : ""
                }`}
                onClick={() => handleDrumClick(beat)}
              >
                {beat}
              </div>
            ))}
        </div>
        <div className="DrumRow">
          {Object.keys(sounds)
            .slice(4, 9)
            .map((beat) => (
              <div
                key={beat}
                className={`Drum ${currentBeat === beat ? "active" : ""} ${
                  isPlayingPattern ? "disabled" : ""
                }`}
                onClick={() => handleDrumClick(beat)}
              >
                {beat}
              </div>
            ))}
        </div>
      </div>
      <div className="ButtonContainer">
        {isGameStarted ? (
          <>
            <CommonButton onClick={resetGame}>다시 하기</CommonButton>
            <CommonButton
              onClick={() => playPattern(pattern, level)}
              disabled={isPlayingPattern || gameOver || pattern.length === 0}
            >
              다시 듣기
            </CommonButton>
          </>
        ) : (
          <CommonButton
            onClick={startPatternGame}
            disabled={isPlayingPattern && !gameOver}
          >
            시작
          </CommonButton>
        )}
      </div>
    </div>
  );
};

export default GameDrum;
