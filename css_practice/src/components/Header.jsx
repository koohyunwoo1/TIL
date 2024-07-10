import "../styles/Header.css";

const Header = ({ title }) => {
  return (
    <header className="Header">
      <div>{title}</div>
    </header>
  );
};

export default Header;
