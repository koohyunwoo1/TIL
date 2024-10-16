import Greeting from "../Components/greeting";

const ParentComponent = () => {
  return <Greeting name="Alice" age={22} isStudent={true} />;
};

export default ParentComponent;
