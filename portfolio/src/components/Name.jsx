import React, { useEffect, useState } from "react";
import "../style/Components/Name.css";

const Name = () => {
  const [displayedText, setDisplayedText] = useState("");
  const fullText = `Hw's PortFolio`;
  const delay = 100;

  useEffect(() => {
    let index = 0;
    const displayNextCharacter = () => {
      if (index < fullText.length) {
        setDisplayedText((prev) => prev + fullText.charAt(index));
        index++;
        setTimeout(displayNextCharacter, delay);
      }
    };

    displayNextCharacter();

    return () => clearTimeout();
  }, []);

  return <div className="Name">{displayedText}</div>;
};

export default Name;
