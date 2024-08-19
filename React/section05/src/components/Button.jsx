const Button = ({ text, color, children }) => {
  // 이벤트 객체
  const onClickButton = (e) => {
    console.log(e);
    // SyntheticBaseEvent
    // 브라우저가 다 다르기 때문에
    // 다 통합된 규격의  합성이벤트
    console.log(text);
  };
  return (
    <button
      onClick={onClickButton}
      // onMouseEnter = {onClickButton}
      style={{ color: color }}
    >
      {text} - {color.toUpperCase()}
      {children}
    </button>
  );
};

Button.defaultProps = {
  // 기본값 설정
  color: "black",
};

export default Button;
