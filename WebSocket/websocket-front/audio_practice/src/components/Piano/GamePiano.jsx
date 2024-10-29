import { useState } from "react";
import "../../style/Piano/GamePiano.css";
import Button from "../Common/Button";
import useNote from "../../hooks/Piano/useNote";
import useChord from "../../hooks/Piano/useChord";

const GamePiano = () => {
  const [mode, setMode] = useState(null);
  const {
    setOctave,
    userInput,
    setUserInput,
    message: noteMessage,
    playRandomNote,
    checkNoteAnswer,
  } = useNote();
  const {
    options,
    message: chordMessage,
    playRandomChord,
    checkChordAnswer,
    level,
    correctCount,
    gameOver,
    resetGame,
    handleNextLevel,
    isAnswered,
  } = useChord();

  return (
    <div className="GamePianoContainer">
      <div className="GamePianoTitle">
        절대 음감
        <img src="/assets/note.png" alt="Note Icon" />
      </div>

      {gameOver ? (
        <div className="GameOverMessage">
          <p>{`게임이 끝났습니다! 맞춘 개수: ${correctCount}`}</p>
          <Button onClick={resetGame}>게임 다시 시작하기</Button>
        </div>
      ) : (
        <>
          {mode === null && (
            <div className="ModeSelect">
              <Button onClick={() => setMode("note")}>음정 맞추기</Button>
              <Button onClick={() => setMode("chord")}>코드 맞추기</Button>
            </div>
          )}

          {mode === "note" && (
            <div className="NoteGuessing">
              <div className="OctaveSelect">
                <Button
                  onClick={() => {
                    setOctave("1옥타브");
                    playRandomNote();
                  }}
                >
                  1옥타브
                </Button>
                <Button
                  onClick={() => {
                    setOctave("2옥타브");
                    playRandomNote();
                  }}
                >
                  2옥타브
                </Button>
                <Button
                  onClick={() => {
                    setOctave("3옥타브");
                    playRandomNote();
                  }}
                >
                  3옥타브
                </Button>
              </div>
              <input
                type="text"
                value={userInput}
                onChange={(e) => setUserInput(e.target.value)}
                placeholder="정답 입력 (ex. C4)"
              />
              <Button onClick={checkNoteAnswer}>제출</Button>
              <div className="MessageDisplay">{noteMessage}</div>
            </div>
          )}

          {mode === "chord" && (
            <>
              <div className="ChordGuessing">
                <div className="PianoLevelDisplay">
                  점수: {correctCount * 10} &nbsp; 단계: {level}
                </div>

                <div className="PianoMessageDisplay">{chordMessage}</div>

                <div className="PianoOptions">
                  {!isAnswered &&
                    options.map((option) => (
                      <Button
                        key={option}
                        onClick={() => checkChordAnswer(option)}
                      >
                        {option}
                      </Button>
                    ))}
                </div>
              </div>
              <div className="PianoGameButton">
                {isAnswered ? (
                  <Button onClick={handleNextLevel}>다음 문제로 가기</Button>
                ) : (
                  <Button onClick={playRandomChord}>코드 듣기</Button>
                )}
              </div>
            </>
          )}
        </>
      )}
    </div>
  );
};

export default GamePiano;
