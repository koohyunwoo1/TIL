import { useState } from "react";
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

  const playSound = (soundType) => {
    sounds[soundType].currentTime = 0;
    sounds[soundType].play();
    console.log(`${soundType} 소리 재생`);
    setCurrentBeat(soundType);
  };

  const handleDrumClick = (drumType) => {
    playSound(drumType);
  };

  return (
    <div className="GameDrumContainer">
      <div className="GameDrumTitle">드럼 비트 재생</div>

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
    </div>
  );
};

export default GameDrum;
