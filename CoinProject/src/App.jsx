import useCoinData from "./hooks/useCoinData";
import Table from "./components/Table";
import Header from "./components/Header";
import Graph from "./components/Graph";
import "./App.css";

const App = () => {
  const { coinData, error } = useCoinData();

  return (
    <>
      <header>
        <Header />
      </header>
      <div className="AppContainer">
        <div className="graph">
          <Graph />
        </div>
        <div className="table">
          <Table coinData={coinData} error={error} />
        </div>
      </div>
    </>
  );
};

export default App;
