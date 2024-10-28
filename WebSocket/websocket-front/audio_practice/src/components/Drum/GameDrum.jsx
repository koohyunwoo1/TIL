import { useState, useEffect } from "react";
import "../../style/Drum/GameDrum.css";

// 지금 문제

// 1. 다음단계로 넘어갈때 전에 드럼을 친 흔적이 남는다.
// 2. 게임이 종료가 되고 나서 다시 하기 다시 듣기 버튼이 활성화 되지 않는다.

const sounds = {
  kick: new Audio("/sounds/kick.wav"),
  snare: new Audio("/sounds/snare.wav"),
  clap: new Audio("/sounds/clap.wav"),
  hihat: new Audio("/sounds/hihat.wav"),
  openhat: new Audio("/sounds/openhat.wav"),
  ride: new Audio("/sounds/ride.wav"),
  boom: new Audio("/sounds/boom.wav"),
  tink: new Audio("/sounds/tink.wav"),
  tom: new Audio("/sounds/tom.wav"),
};

const GameDrum = () => {
  const [currentBeat, setCurrentBeat] = useState(null);
  // 현재 비트
  const [score, setScore] = useState(0);
  // 점수
  const [pattern, setPattern] = useState([]);
  // 비트 패턴
  const [userPattern, setUserPattern] = useState([]);
  // 유저가 입력하는 패턴
  const [isPlayingPattern, setIsPlayingPattern] = useState(false);
  // 패턴이 실행중인지 ?
  const [message, setMessage] = useState(" ");
  // 메세지
  const [level, setLevel] = useState(9);
  // 단계
  const [correctCount, setCorrectCount] = useState(0);
  // 맞은 갯수
  const [gameOver, setGameOver] = useState(false);
  // 게임 끝
  const [isGameStarted, setIsGameStarted] = useState(false);
  // 게임이 시작했는지 ?

  // 주어진 드럼 소리를 재생하는 함수
  const playSound = (soundType) => {
    sounds[soundType].currentTime = 0;
    sounds[soundType].play();
    setCurrentBeat(soundType);
  };

  // 드럼 클릭 시 소리 재생 및 사용자 패턴에 추가하는 함수
  const handleDrumClick = (drumType) => {
    if (isPlayingPattern) return;
    playSound(drumType);
    setUserPattern((prev) => [...prev, drumType]);
  };

  // 랜덤 패턴을 생성하는 함수
  const generateRandomPattern = (length) => {
    const drumTypes = [
      "kick",
      "snare",
      "clap",
      "hihat",
      "openhat",
      "ride",
      "boom",
      "tink",
      "tom",
    ];
    const newPattern = Array.from(
      { length },
      () => drumTypes[Math.floor(Math.random() * drumTypes.length)]
    );
    return newPattern;
  };

  // 생성된 패턴을 재생하는 함수
  const playPattern = (pattern, level) => {
    setTimeout(() => {
      setIsPlayingPattern(true);
      let delay = 0;
      const initialDelay = Math.max(800 - level * 100, 100);

      pattern.forEach((beat, index) => {
        setMessage("잘 들어보세요 !");
        setTimeout(() => {
          playSound(beat);
          if (index === pattern.length - 1) {
            setTimeout(() => {
              setIsPlayingPattern(false);
              setMessage("이제 드럼을 따라 쳐보세요 !");
            }, 1000);
          }
        }, delay);
        delay += initialDelay;
      });
    }, 1000);
  };

  // 게임을 시작하는 함수
  const startPatternGame = () => {
    if (level > 9) {
      setMessage(`게임이 끝났습니다! ${correctCount}/${level}개 맞췄습니다.`);
      setLevel(10);
      setGameOver(true);
      return;
    }
    const newPattern = generateRandomPattern(level + 2);
    setPattern(newPattern);
    setUserPattern([]);
    setMessage("");
    setIsGameStarted(true);
    playPattern(newPattern, level);
  };

  // 게임을 리셋하는 함수
  const resetGame = () => {
    setScore(0);
    setLevel(1);
    setCorrectCount(0);
    setUserPattern([]);
    setMessage("");
    setPattern([]);
    setGameOver(false);
    setIsGameStarted(false);
    setIsPlayingPattern(false);
  };

  // 사용자 패턴을 체크하는 useEffect
  useEffect(() => {
    if (userPattern.length === pattern.length && pattern.length > 0) {
      const isCorrect = userPattern.every(
        (beat, index) => beat === pattern[index]
      );

      if (isCorrect) {
        setMessage("정답입니다!");
        setScore(score + 10);
        setCorrectCount(correctCount + 1);
        setLevel(level + 1);
        setIsPlayingPattern(true);
      } else {
        setMessage("오답입니다! 다음 단계로 넘어갑니다.");
        setLevel(level + 1);
        setIsPlayingPattern(true);
      }

      if (level >= 10) {
        setLevel(10);
        setMessage("게임이 끝났습니다!");
        setGameOver(true);
      }

      setTimeout(() => {
        if (!gameOver) startPatternGame();
      }, 1000);
    }
  }, [userPattern]);

  return (
    <div className="GameDrumContainer">
      <div className="GameDrumTitle">리듬 킹</div>
      {isGameStarted && (
        <>
          <div className="ScoreLevelContainer">
            <div className="ScoreDisplay">점수: {score}</div>
            <div className="LevelDisplay">단계: {level}</div>
          </div>
          <div className="DrumMessageDisplay">{message}</div>
        </>
      )}

      <div className="DrumContainer">
        {["kick", "snare", "clap", "hihat"].map((beat) => (
          <div
            key={beat}
            className={`Drum ${currentBeat === beat ? "active" : ""} ${
              isPlayingPattern ? "disabled" : ""
            }`}
            onClick={() => handleDrumClick(beat)}
          >
            {beat === "kick"
              ? "킥 드럼"
              : beat === "snare"
              ? "스네어 드럼"
              : beat === "clap"
              ? "클랩"
              : "하이햇"}
          </div>
        ))}
      </div>

      <div className="DrumContainer">
        {["openhat", "ride", "boom", "tink", "tom"].map((beat) => (
          <div
            key={beat}
            className={`Drum ${currentBeat === beat ? "active" : ""} ${
              isPlayingPattern ? "disabled" : ""
            }`}
            onClick={() => handleDrumClick(beat)}
          >
            {beat === "openhat"
              ? "오픈햇"
              : beat === "ride"
              ? "라이드 심벌"
              : beat === "boom"
              ? "붐"
              : beat === "tink"
              ? "팅크"
              : "톰"}
          </div>
        ))}
      </div>

      <div>
        {isGameStarted ? (
          <>
            <button
              className="ReplayButton"
              onClick={resetGame}
              disabled={isPlayingPattern}
              // disabled이 true일때 다시하기 버튼이 비활성화된다.
              // 즉 isPlayingPattern이 false면 버튼이 활성화
            >
              다시 하기
            </button>
            <button
              className="ReplayButton"
              onClick={() => playPattern(pattern, level)}
              disabled={isPlayingPattern || gameOver || pattern.length === 0}
            >
              다시 듣기
            </button>
          </>
        ) : (
          <button
            className="StartGameButton"
            onClick={startPatternGame}
            disabled={isPlayingPattern && !gameOver}
          >
            시작
          </button>
        )}
      </div>
    </div>
  );
};

export default GameDrum;
