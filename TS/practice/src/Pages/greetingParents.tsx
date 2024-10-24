import Greeting from "../components/greeting";

const ParentComponent = () => {
  return <Greeting name="Alice" age={22} isStudent={true} />;
};

export default ParentComponent;
