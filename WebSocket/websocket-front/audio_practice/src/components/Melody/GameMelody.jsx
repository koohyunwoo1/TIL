import { useState } from "react";
import PitchFinder from "pitchfinder";
import "../../style/Melody/GameMelody.css";
const GameMelody = () => {
  const [audioContext, setAudioContext] = useState(null);
  const [microphone, setMicrophone] = useState(null);
  const [analyser, setAnalyser] = useState(null);
  const [message, setMessage] = useState("음성을 입력하세요");
  const [currentNote, setCurrentNote] = useState(null);
  const [targetNote, setTargetNote] = useState("C4"); // 기본 미션
  const [isGameActive, setIsGameActive] = useState(false); // 게임 상태 관리
  let interval = null; // interval 변수 추가

  const initMicrophone = async () => {
    try {
      const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      const micStream = await navigator.mediaDevices.getUserMedia({
        audio: true,
      });
      const analyserNode = audioCtx.createAnalyser();
      const micSource = audioCtx.createMediaStreamSource(micStream);
      micSource.connect(analyserNode);

      setAudioContext(audioCtx);
      setMicrophone(micSource);
      setAnalyser(analyserNode);
    } catch (error) {
      console.error("Error accessing microphone", error);
    }
  };

  const stopMicrophone = () => {
    if (microphone && audioContext) {
      microphone.mediaStream.getTracks().forEach((track) => track.stop()); // 마이크 스트림 해제
      audioContext.close(); // 오디오 컨텍스트 종료
      setMicrophone(null);
      setAudioContext(null);
      setAnalyser(null);
    }
  };

  const analyzePitch = () => {
    if (analyser) {
      const detectPitch = new PitchFinder.YIN();
      const buffer = new Float32Array(analyser.fftSize);
      analyser.getFloatTimeDomainData(buffer);

      const pitch = detectPitch(buffer);
      if (pitch) {
        const note = convertToNote(pitch);
        setCurrentNote(note);
        checkAnswer(note); // 미션에 맞는지 체크
      }
    }
  };

  const convertToNote = (frequency) => {
    const notes = [
      "C",
      "C#",
      "D",
      "D#",
      "E",
      "F",
      "F#",
      "G",
      "G#",
      "A",
      "A#",
      "B",
    ];
    const octave = Math.floor(Math.log2(frequency / 440) + 4);
    const noteIndex = Math.round(12 * Math.log2(frequency / 440)) % 12;
    return notes[noteIndex] + octave;
  };

  const checkAnswer = (note) => {
    if (note === targetNote) {
      setMessage("Perfect!");
    } else if (note < targetNote) {
      setMessage("더 높게!");
    } else {
      setMessage("더 낮게!");
    }
  };

  const startGame = async () => {
    if (!isGameActive) {
      // 게임 시작
      setMessage("음성을 입력하세요...");
      await initMicrophone(); // 마이크 활성화
      setIsGameActive(true);
      interval = setInterval(analyzePitch, 100);
    } else {
      // 게임 종료
      setIsGameActive(false);
      setMessage("게임 종료");
      setCurrentNote(null); // 게임 종료 후 현재 음정 리셋
      stopMicrophone(); // 마이크 비활성화
      clearInterval(interval); // interval 해제
    }
  };

  return (
    <div className="GameMelodyContainer">
      <div className="GameMelodyTitle">게임 음정 페이지</div>
      <div className="Mission">미션: {targetNote} 음 맞추기</div>

      <div className="NoteDisplay">
        {currentNote ? `현재 음정: ${currentNote}` : "음성을 감지 중..."}
      </div>

      <button className="start-button" onClick={startGame}>
        {isGameActive ? "게임 끝" : "게임 시작"}
      </button>

      <div
        className={`MessageDisplay ${message === "Perfect!" ? "perfect" : ""}`}
      >
        {currentNote && message}
      </div>
    </div>
  );
};

export default GameMelody;
