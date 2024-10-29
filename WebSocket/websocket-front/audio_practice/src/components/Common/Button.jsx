import "../../style/Common/Button.css";

const CommonButton = ({ children, onClick, disabled }) => {
  return (
    <button className="Button" onClick={onClick} disabled={disabled}>
      {children}
    </button>
  );
};

export default CommonButton;
