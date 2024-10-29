const notes = {
  "1옥타브": ["C4", "D4", "E4", "F4", "G4", "A4", "B4", "C#4", "D#4"],
  "2옥타브": ["C5", "D5", "E5", "F5", "G5", "A5", "B5", "C#5", "D#5"],
  "3옥타브": ["C6", "D6", "E6", "F6", "G6", "A6", "B6", "C#6", "D#6"],
};

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
  { name: "D", notes: ["D5", "F#5", "A5"] },
  { name: "A", notes: ["A4", "C#5", "E5"] },
  { name: "E", notes: ["E5", "G#5", "B5"] },
  { name: "B", notes: ["B4", "D#5", "F#5"] },
  { name: "Cmaj7", notes: ["C5", "E5", "G5", "B5"] },
  { name: "Gmaj7", notes: ["G5", "B5", "D6", "F#6"] },
  { name: "D7", notes: ["D5", "F#5", "A5", "C5"] },
  { name: "B7", notes: ["B4", "D#5", "F#5", "A5"] },
];

export { notes, chords };
