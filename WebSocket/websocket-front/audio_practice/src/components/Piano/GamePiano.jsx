import { useState } from "react";
import "../../style/Piano/GamePiano.css";
import Button from "../Common/Button";
import useNote from "../../hooks/Piano/useNote";
import useChord from "../../hooks/Piano/useChord";

const GamePiano = () => {
  const [mode, setMode] = useState(null);
  const {
    note,
    selectOctave,
    options: noteOptions,
    message: noteMessage,
    playRandomNote,
    checkNoteAnswer,
    level: noteLevel,
    correctCount: noteCorrectCount,
    gameOver: noteGameOver,
    resetGame: resetNoteGame,
    handleNextLevel: handleNextNoteLevel,
    octaveSelected,
    isAnswered: isNoteAnswered,
  } = useNote();

  const {
    options: chordOptions,
    message: chordMessage,
    playRandomChord,
    checkChordAnswer,
    level: chordLevel,
    correctCount: chordCorrectCount,
    gameOver: chordGameOver,
    resetGame: resetChordGame,
    handleNextLevel: handleNextChordLevel,
    isAnswered: isChordAnswered,
  } = useChord();

  return (
    <div className="GamePianoContainer">
      <div className="GamePianoTitle">
        절대 음감
        <img src="/assets/note.png" />
      </div>

      {mode === "note" && noteGameOver ? (
        <>
          <div className="PianoMessageDisplay">{noteMessage}</div>
          <Button onClick={resetNoteGame}>게임 다시 시작하기</Button>
        </>
      ) : mode === "chord" && chordGameOver ? (
        <>
          <div className="PianoMessageDisplay">{chordMessage}</div>
          <Button onClick={resetChordGame}>게임 다시 시작하기</Button>
        </>
      ) : (
        <>
          {mode === null && (
            <div className="ModeSelect">
              <Button onClick={() => setMode("note")}>음정 맞추기</Button>
              <Button onClick={() => setMode("chord")}>화음 맞추기</Button>
            </div>
          )}

          {mode === "note" && (
            <div>
              <div className="PianoLevelDisplay">
                점수: {noteCorrectCount * 10} &nbsp; 단계: {noteLevel}
              </div>

              <div className="PianoMessageDisplay">
                {!octaveSelected ? "옥타브를 선택해주세요!" : noteMessage}
              </div>

              {!octaveSelected && (
                <div className="PianoOptions">
                  <Button onClick={() => selectOctave("1옥타브")}>
                    1옥타브
                  </Button>
                  <Button onClick={() => selectOctave("2옥타브")}>
                    2옥타브
                  </Button>
                  <Button onClick={() => selectOctave("3옥타브")}>
                    3옥타브
                  </Button>
                </div>
              )}

              {octaveSelected && (
                <>
                  <div className="PianoOptions">
                    {!isNoteAnswered &&
                      noteOptions.map((option) => (
                        <Button
                          key={option}
                          onClick={() => checkNoteAnswer(option)}
                        >
                          {option}
                        </Button>
                      ))}
                  </div>

                  <div className="PianoGameButton">
                    {isNoteAnswered ? (
                      <Button onClick={handleNextNoteLevel}>
                        다음 문제로 가기
                      </Button>
                    ) : (
                      <Button onClick={() => playRandomNote(note)}>
                        음 듣기
                      </Button>
                    )}
                  </div>
                </>
              )}
            </div>
          )}

          {mode === "chord" && (
            <div>
              <div className="PianoLevelDisplay">
                점수: {chordCorrectCount * 10} &nbsp; 단계: {chordLevel}
              </div>

              <div className="PianoMessageDisplay">{chordMessage}</div>

              <div className="PianoOptions">
                {!isChordAnswered &&
                  chordOptions.map((option) => (
                    <Button
                      key={option}
                      onClick={() => checkChordAnswer(option)}
                    >
                      {option}
                    </Button>
                  ))}
              </div>

              <div className="PianoGameButton">
                {isChordAnswered ? (
                  <Button onClick={handleNextChordLevel}>
                    다음 문제로 가기
                  </Button>
                ) : (
                  <Button onClick={playRandomChord}>화음 듣기</Button>
                )}
              </div>
            </div>
          )}
        </>
      )}
    </div>
  );
};

export default GamePiano;
