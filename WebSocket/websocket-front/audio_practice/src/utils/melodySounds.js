// 마이크를 초기화하고 오디오 컨텍스트와 분석기를 설정하는 함수
const initMicrophone = async () => {
  try {
    const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    const micStream = await navigator.mediaDevices.getUserMedia({
      audio: true,
    });
    const analyserNode = audioCtx.createAnalyser();
    const micSource = audioCtx.createMediaStreamSource(micStream);
    micSource.connect(analyserNode);

    return { audioCtx, micSource, analyserNode };
  } catch (error) {
    console.error(error);
    throw error;
  }
};

// 마이크를 중지하고 리소스를 해제하는 함수
const stopMicrophone = (audioContext, microphone) => {
  if (microphone && audioContext) {
    microphone.mediaStream.getTracks().forEach((track) => track.stop());

    audioContext.close();
  }
};

// 주어진 주파수를 음으로 변환하는 함수
const convertToNote = (frequency) => {
  const notes = [
    // 1옥타브
    "C1",
    "C#1",
    "D1",
    "D#1",
    "E1",
    "F1",
    "F#1",
    "G1",
    "G#1",
    "A1",
    "A#1",
    "B1",
    // 2옥타브
    "C2",
    "C#2",
    "D2",
    "D#2",
    "E2",
    "F2",
    "F#2",
    "G2",
    "G#2",
    "A2",
    "A#2",
    "B2",
    // 3옥타브
    "C3",
    "C#3",
    "D3",
    "D#3",
    "E3",
    "F3",
    "F#3",
    "G3",
    "G#3",
    "A3",
    "A#3",
    "B3",
    // 4옥타브
    "C4",
    "C#4",
    "D4",
    "D#4",
    "E4",
    "F4",
    "F#4",
    "G4",
    "G#4",
    "A4",
    "A#4",
    "B4",
  ];

  const octave = Math.floor(Math.log2(frequency / 440) + 4);
  const noteIndex = Math.round(12 * Math.log2(frequency / 440)) % 12;

  return notes[noteIndex] + octave;
};

// 함수들을 외부에서 사용할 수 있도록 내보내기
export { initMicrophone, stopMicrophone, convertToNote };
