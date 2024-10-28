import { useState } from "react";
import * as Tone from "tone";
import "../../style/Piano/GamePiano.css";
const notes = ["C4", "D4", "E4", "F4", "G4", "A4", "B4", "C#4", "D#4"];
const chords = [
  { name: "C", notes: ["C4", "E4", "G4"] },
  { name: "G", notes: ["G4", "B4", "D5"] },
  { name: "Am", notes: ["A4", "C5", "E5"] },
  { name: "F", notes: ["F4", "A4", "C5"] },
  { name: "C7", notes: ["C4", "E4", "G4", "Bb4"] },
  { name: "G7", notes: ["G4", "B4", "D5", "F5"] },
  { name: "Dm", notes: ["D4", "F4", "A4"] },
  { name: "C#7", notes: ["C#4", "F4", "G#4", "B4"] },
  { name: "F#m7", notes: ["F#4", "A4", "C#5", "E5"] },
];

const GamePiano = () => {
  const [mode, setMode] = useState(null);
  const [note, setNote] = useState(null);
  const [userInput, setUserInput] = useState("");
  const [message, setMessage] = useState("");
  const [options, setOptions] = useState([]);
  const [correctAnswer, setCorrectAnswer] = useState(null);

  // 음정 재생
  const playNote = async (note) => {
    await Tone.start(); // Tone.js 시작
    const synth = new Tone.Synth().toDestination(); // Synth 생성
    synth.triggerAttackRelease(note, "8n"); // 음정 재생 (8분음표 길이)
  };

  // 랜덤 음정 출제
  const playRandomNote = () => {
    const randomNote = notes[Math.floor(Math.random() * notes.length)];
    setNote(randomNote);
    playNote(randomNote); // 실제 음정 재생
    console.log(`Playing note: ${randomNote}`);
  };

  // 코드 재생
  const playChord = async (chord) => {
    await Tone.start();
    const synth = new Tone.PolySynth().toDestination(); // 다성 음을 위한 PolySynth 생성
    synth.triggerAttackRelease(chord.notes, "2n"); // 코드 재생 (2분음표 길이)
  };

  // 랜덤 코드 출제
  const playRandomChord = () => {
    const randomChord = chords[Math.floor(Math.random() * chords.length)];
    setCorrectAnswer(randomChord.name);
    setOptions(generateOptions(randomChord.name));
    playChord(randomChord); // 실제 코드 재생
    console.log(`Playing chord: ${randomChord.name}`);
  };

  // 정답 검증 (음정 맞추기)
  const checkNoteAnswer = () => {
    if (userInput.toLowerCase() === note.toLowerCase()) {
      // 대소문자 구분 없이 비교
      setMessage("정답입니다!");
    } else {
      setMessage(`오답입니다! 정답은 ${note} 입니다.`);
    }
  };

  // 보기 생성 (코드 맞추기)
  const generateOptions = (correct) => {
    let randomOptions = chords.filter((chord) => chord.name !== correct);
    randomOptions = randomOptions.sort(() => 0.5 - Math.random()).slice(0, 3); // 오답 보기 3개 선택
    return [...randomOptions.map((chord) => chord.name), correct].sort(
      () => 0.5 - Math.random()
    ); // 정답 포함해 섞기
  };

  // 코드 정답 선택
  const checkChordAnswer = (selectedOption) => {
    if (selectedOption === correctAnswer) {
      setMessage("정답입니다!");
    } else {
      setMessage(`오답입니다! 정답은 ${correctAnswer} 입니다.`);
    }
  };

  return (
    <div className="GamePianoContainer">
      <div className="GamePianoTitle">
        절대 음감
        <img src="/assets/note.png" />
      </div>

      <div className="ModeSelect">
        <button onClick={() => setMode("note")}>음정 맞추기</button>
        <button onClick={() => setMode("chord")}>코드 맞추기</button>
      </div>

      {mode === "note" && (
        <div className="NoteGuessing">
          <button onClick={playRandomNote}>음정 들려주기</button>
          <input
            type="text"
            value={userInput}
            onChange={(e) => setUserInput(e.target.value)}
            placeholder="정답 입력 (ex. C4)"
          />
          <button onClick={checkNoteAnswer}>제출</button>
          <div className="MessageDisplay">{message}</div>
        </div>
      )}

      {mode === "chord" && (
        <div className="ChordGuessing">
          <button onClick={playRandomChord}>코드 들려주기</button>
          <div className="Options">
            {options.map((option) => (
              <button key={option} onClick={() => checkChordAnswer(option)}>
                {option}
              </button>
            ))}
          </div>
          <div className="PianoMessageDisplay">{message}</div>
        </div>
      )}
    </div>
  );
};

export default GamePiano;
