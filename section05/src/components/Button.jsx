const Button = ({text, color, children}) => {
  return (
  <button style={{ color: color}}>
    {text} - {color.toUpperCase()}
    {children}
    </button>
)
};

Button.defaultProps = {
  // 기본값 설정
  color : 'black'
}

export default Button;
