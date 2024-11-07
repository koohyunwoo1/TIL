import React from "react";
import "../../style/Common/Modal.css";

const Modal = ({ isVisible, onClose, content }) => {
  if (!isVisible) return null;

  const handleBackgroundClick = (e) => {
    if (e.target.classList.contains("Modal")) {
      onClose();
    }
  };

  return (
    <div className="Modal" onClick={handleBackgroundClick}>
      <div className="ModalContent">
        <button onClick={onClose} className="CloseButton">
          &times;
        </button>
        <div className="ModalBody">{content}</div>
      </div>
    </div>
  );
};

export default Modal;
