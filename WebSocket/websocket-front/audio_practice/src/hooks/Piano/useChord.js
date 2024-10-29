import { useState } from "react";
import { chords } from "../../utils/pianoSound";
import * as Tone from "tone";

const useChord = () => {
  const [correctAnswer, setCorrectAnswer] = useState(null);
  const [options, setOptions] = useState([]);
  const [message, setMessage] = useState("");
  const [level, setLevel] = useState(1);
  const [correctCount, setCorrectCount] = useState(0);
  const [gameOver, setGameOver] = useState(false);
  const [isAnswered, setIsAnswered] = useState(false);
  const [hasPlayedChord, setHasPlayedChord] = useState(false);
  const [currentChord, setCurrentChord] = useState(null);

  const playChord = async (chord) => {
    const synth = new Tone.PolySynth().toDestination();
    synth.triggerAttackRelease(chord.notes, "2n");
  };

  const playRandomChord = () => {
    if (currentChord) {
      playChord(currentChord);
      return;
    }

    const randomChord = chords[Math.floor(Math.random() * chords.length)];
    setCorrectAnswer(randomChord.name);
    setOptions(generateOptions(randomChord.name));
    setCurrentChord(randomChord);
    playChord(randomChord);
    setHasPlayedChord(true);
  };

  const generateOptions = (correct) => {
    let randomOptions = chords.filter((chord) => chord.name !== correct);
    randomOptions = randomOptions.sort(() => 0.5 - Math.random()).slice(0, 3);
    return [...randomOptions.map((chord) => chord.name), correct].sort(
      () => 0.5 - Math.random()
    );
  };

  const checkChordAnswer = (selectedOption) => {
    if (isAnswered) return;

    if (level >= 10) {
      setMessage(`게임이 끝났습니다! ${correctCount * 10}점 입니다 ! .`);
      setGameOver(true);
      return;
    }

    if (selectedOption === correctAnswer) {
      setMessage("정답입니다!");
      setCorrectCount((prev) => prev + 1);
    } else {
      setMessage(`오답입니다! 정답은 ${correctAnswer} 입니다.`);
    }

    setIsAnswered(true);
  };

  const handleNextLevel = () => {
    setLevel((prev) => Math.min(prev + 1, 10));
    setCurrentChord(null);
    setIsAnswered(false);
    setMessage("");
  };

  const resetGame = () => {
    setLevel(1);
    setCorrectCount(0);
    setMessage("");
    setGameOver(false);
    setIsAnswered(false);
    setHasPlayedChord(false);
    setCurrentChord(null);
  };

  return {
    options,
    message,
    playRandomChord,
    checkChordAnswer,
    level,
    correctCount,
    gameOver,
    resetGame,
    handleNextLevel,
    isAnswered,
    hasPlayedChord,
  };
};

export default useChord;
