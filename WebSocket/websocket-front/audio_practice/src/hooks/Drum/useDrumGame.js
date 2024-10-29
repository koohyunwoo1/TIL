import { useState, useEffect, useRef } from "react";
import sounds from "../../utils/drumSound";

const useDrumGame = () => {
  const [currentBeat, setCurrentBeat] = useState(null);
  const [score, setScore] = useState(0);
  const [pattern, setPattern] = useState([]);
  const [userPattern, setUserPattern] = useState([]);
  const [isPlayingPattern, setIsPlayingPattern] = useState(false);
  const [message, setMessage] = useState(" ");
  const [level, setLevel] = useState(1);
  const [correctCount, setCorrectCount] = useState(0);
  const [gameOver, setGameOver] = useState(false);
  const [isGameStarted, setIsGameStarted] = useState(false);
  const timerRefs = useRef([]);

  const playSound = (soundType) => {
    sounds[soundType].currentTime = 0;
    sounds[soundType].play();
    setCurrentBeat(soundType);
  };

  const handleDrumClick = (drumType) => {
    if (isPlayingPattern) return;
    playSound(drumType);
    setUserPattern((prev) => [...prev, drumType]);
  };

  const generateRandomPattern = (length) => {
    const drumTypes = Object.keys(sounds);
    return Array.from(
      { length },
      () => drumTypes[Math.floor(Math.random() * drumTypes.length)]
    );
  };

  const playPattern = (pattern, level) => {
    setUserPattern([]);
    setIsPlayingPattern(true);
    setMessage("잘 들어보세요 !");
    let delay = 0;
    const initialDelay = Math.max(800 - level * 100, 100);
    pattern.forEach((beat, index) => {
      const timerId = setTimeout(() => {
        playSound(beat);
        if (index === pattern.length - 1) {
          setTimeout(() => {
            setIsPlayingPattern(false);
            setMessage("이제 드럼을 따라 쳐보세요 !");
          }, 1000);
        }
      }, delay);
      timerRefs.current.push(timerId);
      delay += initialDelay;
    });
  };

  const startPatternGame = () => {
    if (level > 9) {
      setMessage(`게임이 끝났습니다! ${correctCount * 10}점 입니다 ! `);
      setGameOver(true);
      return;
    }
    const newPattern = generateRandomPattern(level + 2);
    setPattern(newPattern);
    setUserPattern([]);
    setMessage("준비하세요!");
    setIsGameStarted(true);

    setTimeout(() => {
      setMessage("");
      playPattern(newPattern, level);
    }, 1000);
  };

  const resetGame = () => {
    setScore(0);
    setLevel(1);
    setCurrentBeat(null);
    setCorrectCount(0);
    setUserPattern([]);
    setMessage("");
    setPattern([]);
    setGameOver(false);
    setIsGameStarted(false);
    setIsPlayingPattern(false);

    Object.values(sounds).forEach((sound) => {
      sound.pause();
      sound.currentTime = 0;
    });

    timerRefs.current.forEach((id) => clearTimeout(id));
    timerRefs.current = [];
  };

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
        setCurrentBeat(null);
        setIsPlayingPattern(true);
      } else {
        setMessage("오답입니다! 다음 단계로 넘어갑니다.");
        setLevel(level + 1);
        setCurrentBeat(null);
        setIsPlayingPattern(true);
      }
      if (level >= 10) {
        setLevel(10);
        setMessage("게임이 끝났습니다!");
        setCurrentBeat(null);
        setGameOver(true);
      }
      setTimeout(() => {
        if (!gameOver) startPatternGame();
      }, 1000);
    }
  }, [userPattern]);

  useEffect(() => {
    return () => {
      resetGame();
    };
  }, []);

  return {
    currentBeat,
    score,
    pattern,
    userPattern,
    isPlayingPattern,
    message,
    level,
    correctCount,
    gameOver,
    isGameStarted,
    handleDrumClick,
    startPatternGame,
    resetGame,
    playPattern,
  };
};

export default useDrumGame;
