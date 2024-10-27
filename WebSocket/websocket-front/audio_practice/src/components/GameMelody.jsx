import { useState, useEffect } from "react";
import PitchFinder from "pitchfinder";
import "../style/GameMelody.css";

const GameMelody = () => {
  const [audioContext, setAudioContext] = useState(null);
  const [microphone, setMicrophone] = useState(null);
  const [analyser, setAnalyser] = useState(null);
  const [message, setMessage] = useState("음성을 입력하세요");
  const [currentNote, setCurrentNote] = useState(null);
  const [targetNote, setTargetNote] = useState("C4"); // 기본 미션

  useEffect(() => {
    // 컴포넌트가 마운트되면 마이크를 설정합니다.
    const initMicrophone = async () => {
      try {
        const audioCtx = new (window.AudioContext ||
          window.webkitAudioContext)();
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

    initMicrophone();

    return () => {
      if (audioContext) {
        audioContext.close();
      }
    };
  }, []);

  // 음정 분석 로직
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
      setMessage("정답입니다!");
    } else {
      setMessage(`오답입니다! 현재 음: ${note}`);
    }
  };

  const startGame = () => {
    setMessage("음성을 입력하세요...");
    const interval = setInterval(analyzePitch, 100);
    setTimeout(() => clearInterval(interval), 10000);
  };

  return (
    <div className="GameMelodyContainer">
      <div className="GameMelodyTitle">게임 음정 페이지</div>
      <div className="Mission">미션: {targetNote} 음 맞추기</div>
      <button className="start-button" onClick={startGame}>
        게임 시작
      </button>
      <div className="MessageDisplay">{message}</div>
    </div>
  );
};

export default GameMelody;
