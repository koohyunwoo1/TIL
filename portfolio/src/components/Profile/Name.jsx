import React, { useEffect, useState } from "react";
import "../../style/Components/Name.css";

const Name = ({ onComplete }) => {
  const [displayedText, setDisplayedText] = useState("");
  const fullText = `HyunWoo\nPORTFOLIO`;
  const delay = 100;

  useEffect(() => {
    let index = 0;

    const displayNextCharacter = () => {
      if (index < fullText.length) {
        if (fullText.charAt(index) === "\n") {
          setDisplayedText((prev) => prev + "<br />");
        } else {
          setDisplayedText((prev) => prev + fullText.charAt(index));
        }

        setTimeout(() => {
          index++;
          displayNextCharacter();
        }, delay);
      } else {
        onComplete();
      }
    };

    displayNextCharacter();
  }, []);

  return (
    <div className="Name" dangerouslySetInnerHTML={{ __html: displayedText }} />
  );
};

export default Name;
