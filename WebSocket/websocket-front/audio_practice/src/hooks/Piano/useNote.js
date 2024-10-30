import { useState, useEffect } from "react";
import { notes } from "../../utils/pianoSound";
import * as Tone from "tone";

const useNote = () => {
  const [octave, setOctave] = useState(null); // 선택된 옥타브를 null로 초기화
  console.log(octave);
  const [note, setNote] = useState(null); // 현재 정답 음
  const [options, setOptions] = useState([]); // 선택지
  const [message, setMessage] = useState(""); // 피드백 메시지
  const [level, setLevel] = useState(1); // 현재 레벨
  const [correctCount, setCorrectCount] = useState(0); // 정답 수 카운트
  const [gameOver, setGameOver] = useState(false); // 게임 종료 여부
  const [isAnswered, setIsAnswered] = useState(false); // 현재 문제의 답변 여부
  const [octaveSelected, setOctaveSelected] = useState(false); // 옥타브 선택 여부
  const [hasPlayedNote, setHasPlayedNote] = useState(false); // 음이 재생되었는지 여부
  const [isDisabled, setIsDisabled] = useState(true); // 선택지 비활성화

  // 음을 재생하는 함수
  const playNote = async (note) => {
    const synth = new Tone.Synth().toDestination();
    synth.triggerAttackRelease(note, "8n");
    setHasPlayedNote(true);
  };

  // 음 재생 요청 함수 - 버튼 클릭 시 실행됨
  const playRandomNote = () => {
    if (note) {
      playNote(note);
      setHasPlayedNote(true);
      setIsDisabled(false);
    }
  };

  // 옥타브 선택 시 호출되는 함수
  const selectOctave = (oct) => {
    console.log(oct);
    setOctave(oct);
    setOctaveSelected(true);
    generateNewQuestion();
  };

  // 새로운 문제를 생성하는 함수 (랜덤한 음과 선택지를 설정)
  const generateNewQuestion = () => {
    if (!octave) {
      setMessage("먼저 옥타브를 선택하세요!");
      return;
    }
    const selectedNotes = notes[octave];
    const randomNote =
      selectedNotes[Math.floor(Math.random() * selectedNotes.length)];
    setNote(randomNote);
    setOptions(generateOptions(randomNote));
    setIsAnswered(false);
    setHasPlayedNote(false);
    setIsDisabled(true);
    setMessage("음 듣기를 눌러 음을 들어주세요 !");
  };

  useEffect(() => {
    if (octave) {
      generateNewQuestion();
    }
  }, [octave]);

  // 선택지 3가지를 랜덤으로 생성하여 리턴하는 함수
  const generateOptions = (correct) => {
    let randomOptions = notes[octave].filter((n) => n !== correct);
    randomOptions = randomOptions.sort(() => 0.5 - Math.random()).slice(0, 3);
    return [...randomOptions, correct].sort(() => 0.5 - Math.random());
  };

  // 사용자의 선택이 정답인지 확인하고 피드백을 제공하는 함수
  const checkNoteAnswer = (selectedOption) => {
    if (isAnswered) return;

    if (!hasPlayedNote) {
      setMessage("먼저 음을 들어야 합니다 !");
      return;
    }

    if (level >= 10) {
      setMessage(`게임이 끝났습니다! ${correctCount * 10}점 입니다 !`);
      setGameOver(true);
      return;
    }

    if (selectedOption === note) {
      setMessage("정답입니다!");
      setCorrectCount((prev) => prev + 1);
    } else {
      setMessage(`오답입니다! 정답은 ${note} 입니다.`);
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
    setHasPlayedNote(false);
    setNote(null);
    setIsDisabled(true);
    setOctaveSelected(false);
    setOctave(null);
    generateNewQuestion();
  };

  return {
    octave,
    selectOctave,
    options,
    message,
    playNote,
    checkNoteAnswer,
    level,
    correctCount,
    gameOver,
    resetGame,
    handleNextLevel,
    octaveSelected,
    isAnswered,
    isDisabled,
    playRandomNote,
    hasPlayedNote,
  };
};

export default useNote;
