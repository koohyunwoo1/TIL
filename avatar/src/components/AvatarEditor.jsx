// src/components/AvatarEditor.js

import React, { useRef, useState } from "react";
import AvatarEditor from "react-avatar-editor";

const AvatarEditorComponent = () => {
  const editorRef = useRef(null);
  const [image, setImage] = useState("");
  const [scale, setScale] = useState(1.2);

  const handleImageChange = (e) => {
    setImage(e.target.files[0]);
  };

  const handleScaleChange = (e) => {
    setScale(parseFloat(e.target.value));
  };

  const handleSave = () => {
    if (editorRef.current) {
      const canvas = editorRef.current.getImageScaledToCanvas().toDataURL();
      console.log(canvas); // Save the avatar data URL or send it to a server
    }
  };

  return (
    <div>
      <input type="file" onChange={handleImageChange} />
      <input
        type="range"
        min="1"
        max="2"
        step="0.01"
        value={scale}
        onChange={handleScaleChange}
      />
      <AvatarEditor
        ref={editorRef}
        image={image}
        width={250}
        height={250}
        border={50}
        scale={scale}
      />
      <button onClick={handleSave}>Save Avatar</button>
    </div>
  );
};

export default AvatarEditorComponent;
