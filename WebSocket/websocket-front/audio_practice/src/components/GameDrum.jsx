import React, { useState, useEffect } from "react";
import "../style/GameDrum.css";

// 사운드 파일 경로를 정의합니다.
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
  const [score, setScore] = useState(0);
  const [currentBeat, setCurrentBeat] = useState(null); // 현재 비트
  const [playing, setPlaying] = useState(false);
  const beatOptions = ["kick", "snare", "clap", "hihat"]; // 사용할 수 있는 비트 종류

  useEffect(() => {
    if (playing) {
      const interval = setInterval(() => {
        const randomBeat =
          beatOptions[Math.floor(Math.random() * beatOptions.length)];
        setCurrentBeat(randomBeat); // 랜덤 비트 설정
        playSound(randomBeat); // 비트 재생
      }, 1000); // 1초마다 비트 재생

      return () => clearInterval(interval);
    }
  }, [playing]);

  const playSound = (soundType) => {
    sounds[soundType].currentTime = 0; // 사운드 재생 전 시간 초기화
    sounds[soundType].play(); // 사운드 재생
    console.log(`${soundType} 소리 재생`); // 현재는 콘솔 로그로 대체
  };

  const handleDrumClick = (drumType) => {
    if (drumType === currentBeat) {
      setScore(score + 10); // 점수 추가
      console.log("정답! 점수:", score + 10);
    } else {
      setScore(score - 5); // 점수 차감
      console.log("오답! 점수:", score - 5);
    }
  };

  return (
    <div className="GameDrumContainer">
      <div className="GameDrumTitle">드럼 비트 챌린지</div>
      <div className="ScoreDisplay">점수: {score}</div>
      <button onClick={() => setPlaying(!playing)}>
        {playing ? "중지" : "시작"}
      </button>
      <div className="DrumContainer">
        <div className="Drum" onClick={() => handleDrumClick("kick")}>
          킥
        </div>
        <div className="Drum" onClick={() => handleDrumClick("snare")}>
          스네어
        </div>
        <div className="Drum" onClick={() => handleDrumClick("clap")}>
          박수
        </div>
        <div className="Drum" onClick={() => handleDrumClick("hihat")}>
          하이햇
        </div>
      </div>
      <div className="CurrentBeatDisplay">
        현재 비트: {currentBeat ? currentBeat.toUpperCase() : "없음"}
      </div>
    </div>
  );
};

export default GameDrum;
