import { useState } from "react";
import { notes } from "../../utils/pianoSound";
import * as Tone from "tone";

const useNote = () => {
  const [octave, setOctave] = useState("1옥타브");
  const [note, setNote] = useState(null);
  const [userInput, setUserInput] = useState("");
  const [message, setMessage] = useState("");

  const playNote = async (note) => {
    const synth = new Tone.Synth().toDestination();
    synth.triggerAttackRelease(note, "8n");
  };

  const playRandomNote = () => {
    const selectedNotes = notes[octave];
    const randomNote =
      selectedNotes[Math.floor(Math.random() * selectedNotes.length)];
    setNote(randomNote);
    playNote(randomNote);
  };

  const checkNoteAnswer = () => {
    if (userInput.toLowerCase() === note.toLowerCase()) {
      setMessage("정답입니다!");
    } else {
      setMessage(`오답입니다! 정답은 ${note} 입니다.`);
    }
  };

  return {
    octave,
    setOctave,
    userInput,
    setUserInput,
    message,
    playRandomNote,
    checkNoteAnswer,
  };
};

export default useNote;
