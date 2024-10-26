import { useState, useEffect } from "react";
import "../style/GameDrum.css";

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
  const [playing, setPlaying] = useState(false);
  const [beatCount, setBeatCount] = useState(0);
  const [messages, setMessages] = useState("");
  const [intervalDuration, setIntervalDuration] = useState(1000);

  const beatOptions = [
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

  useEffect(() => {
    if (playing) {
      const interval = setInterval(() => {
        const randomBeat =
          beatOptions[Math.floor(Math.random() * beatOptions.length)];
        setCurrentBeat(randomBeat);
        playSound(randomBeat);
        setBeatCount((prev) => prev + 1);

        // 2개의 비트가 끝났을 때 메시지 변경
        if (beatCount >= 1) {
          setMessages("이제 따라쳐보세요!");
          clearInterval(interval);
          setPlaying(false); // 비트가 끝나면 게임 종료
        } else {
          setMessages("잘 들어보세요!");
        }
      }, intervalDuration);

      return () => clearInterval(interval);
    }
  }, [playing, intervalDuration, beatCount]);

  const playSound = (soundType) => {
    sounds[soundType].currentTime = 0;
    sounds[soundType].play();
    console.log(`${soundType} 소리 재생`);
  };

  const handleDrumClick = (drumType) => {
    playSound(drumType);
  };

  const resetGame = () => {
    setBeatCount(0);
    setIntervalDuration(1000);
    setMessages("");
    setPlaying(false);
  };

  return (
    <div className="GameDrumContainer">
      <div className="GameDrumTitle">드럼 비트 챌린지</div>
      <button onClick={() => setPlaying(!playing)} className="DrumButton">
        {playing ? "중지" : "시작"}
      </button>

      <div className="DrumContainer">
        <div className="Drum" onClick={() => handleDrumClick("kick")}>
          킥 드럼
        </div>
        <div className="Drum" onClick={() => handleDrumClick("snare")}>
          스네어 드럼
        </div>
        <div className="Drum" onClick={() => handleDrumClick("clap")}>
          클랩
        </div>
        <div className="Drum" onClick={() => handleDrumClick("hihat")}>
          하이햇
        </div>
      </div>

      <div className="DrumContainer">
        <div className="Drum" onClick={() => handleDrumClick("openhat")}>
          오픈햇
        </div>
        <div className="Drum" onClick={() => handleDrumClick("ride")}>
          라이드 심벌
        </div>
        <div className="Drum" onClick={() => handleDrumClick("boom")}>
          붐
        </div>
        <div className="Drum" onClick={() => handleDrumClick("tink")}>
          팅크
        </div>
        <div className="Drum" onClick={() => handleDrumClick("tom")}>
          톰
        </div>
      </div>

      <div className="CurrentBeatDisplay">
        현재 비트: {currentBeat ? currentBeat.toUpperCase() : "없음"}
      </div>

      <div className="MessageDisplay">{messages}</div>
    </div>
  );
};

export default GameDrum;
