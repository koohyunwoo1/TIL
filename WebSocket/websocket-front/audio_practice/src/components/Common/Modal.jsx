import "../../style/Common/Modal.css";

const Modal = ({ isOpen, onClose, children }) => {
  if (!isOpen) return null;

  return (
    <div className="modalOverlay" onClick={onClose}>
      <div className="modalContent" onClick={(e) => e.stopPropagation()}>
        {children}
        <button className="modalCloseButton" onClick={onClose}>
          X
        </button>
      </div>
    </div>
  );
};

export default Modal;
