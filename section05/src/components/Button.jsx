const Button = ({text, color}) => {
  return (
  <button style={{ color: color}}>
    {text} - {color.toUpperCase()}
    </button>
)
};

Button.defaultProps = {
  // 기본값 설정
  color : 'black'
}

export default Button;
