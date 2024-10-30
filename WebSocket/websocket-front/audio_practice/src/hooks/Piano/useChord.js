import { useEffect, useState } from "react";
import { chords } from "../../utils/pianoSound";
import * as Tone from "tone";

const useChord = () => {
  const [correctAnswer, setCorrectAnswer] = useState(null); // 현재 문제의 정답
  const [options, setOptions] = useState([]); // 선택지
  const [message, setMessage] = useState(""); // 피드백 메시지
  const [level, setLevel] = useState(1); // 현재 레벨
  const [correctCount, setCorrectCount] = useState(0); // 정답 수 카운트
  const [gameOver, setGameOver] = useState(false); // 게임 종료 여부
  const [isAnswered, setIsAnswered] = useState(false); // 현재 문제의 답변 여부
  const [hasPlayedChord, setHasPlayedChord] = useState(false); // 코드가 재생되었는지 여부
  const [currentChord, setCurrentChord] = useState(null); // 현재 재생 중인 코드
  const [isDisabled, setIsDisabled] = useState(true); // 선택지 비활성화 여부

  // 특정 코드를 재생하는 함수
  const playChord = async (chord) => {
    const synth = new Tone.PolySynth().toDestination();
    synth.triggerAttackRelease(chord.notes, "2n");
  };

  // 코드 재생 요청 함수 - 버튼 클릭 시 실행됨
  const playRandomChord = () => {
    if (currentChord) {
      playChord(currentChord);
      setHasPlayedChord(true);
      setIsDisabled(false);
    }
  };

  // 새로운 문제를 설정하는 함수 (코드를 재생하지 않고 문제와 선택지만 업데이트)
  const generateNewQuestion = () => {
    const randomChord = chords[Math.floor(Math.random() * chords.length)];
    setCorrectAnswer(randomChord.name);
    setOptions(generateOptions(randomChord.name));
    setCurrentChord(randomChord);
    setHasPlayedChord(false);
    setIsDisabled(true);
    setMessage("화음 듣기를 먼저 눌러 화음을 들어주세요 !");
  };

  // 정답 외에 선택지 3가지를 랜덤으로 생성하여 리턴하는 함수
  const generateOptions = (correct) => {
    let randomOptions = chords.filter((chord) => chord.name !== correct);
    randomOptions = randomOptions.sort(() => 0.5 - Math.random()).slice(0, 3);
    return [...randomOptions.map((chord) => chord.name), correct].sort(
      () => 0.5 - Math.random()
    );
  };

  // 사용자의 선택이 정답인지 확인하고 피드백을 제공하는 함수
  const checkChordAnswer = (selectedOption) => {
    if (isAnswered) return;

    if (!hasPlayedChord) {
      setMessage("먼저 화음을 들어야 합니다 !");
      return;
    }

    if (level >= 10) {
      setMessage(`게임이 끝났습니다! ${correctCount * 10}점 입니다 !`);
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

  // 다음 문제로 넘어가는 함수
  const handleNextLevel = () => {
    setLevel((prev) => Math.min(prev + 1, 10));
    setIsAnswered(false);
    setMessage("");
    generateNewQuestion();
  };

  // 게임을 초기 상태로 리셋하는 함수
  const resetGame = () => {
    setLevel(1);
    setCorrectCount(0);
    setMessage("");
    setGameOver(false);
    setIsAnswered(false);
    setHasPlayedChord(false);
    setCurrentChord(null);
    setIsDisabled(true);
    generateNewQuestion();
    // setOptions([]);
  };

  useEffect(() => {
    generateNewQuestion();
  }, []);

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
    isDisabled,
  };
};

export default useChord;
