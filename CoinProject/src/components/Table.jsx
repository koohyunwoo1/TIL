import "../style/Table.css";
import { FiSearch } from "react-icons/fi";
import useTableLogic from "../hooks/useTableLogic";
import useSearch from "../hooks/useSearch";

const Table = ({ coinData, error }) => {
  const { searchTerm, setSearchTerm, filteredData } = useSearch(coinData);

  const {
    sortedData,
    handleSort,
    getChangeRateColor,
    getCurrentPriceColor,
    formatTradeVolume,
  } = useTableLogic(filteredData);

  if (error) return <p style={{ color: "red" }}>{error}</p>;

  return (
    <div className="TableContainer">
      <div className="TableWrapper">
        <div className="SearchContainer">
          <div className="SearchInputWrapper">
            <FiSearch className="SearchIcon" />
            <input
              type="text"
              className="SearchInput"
              placeholder="코인명/심볼 검색"
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
            />
          </div>
        </div>
        <table>
          <thead>
            <tr>
              <th onClick={() => handleSort("koreanName")}>한글명</th>
              <th onClick={() => handleSort("currentPrice")}>현재가</th>
              <th onClick={() => handleSort("changeRate")}>전일대비</th>
              <th onClick={() => handleSort("tradeVolume")}>거래대금</th>
            </tr>
          </thead>
          <tbody>
            {sortedData.map((coin, index) => (
              <tr key={index}>
                <td>{coin.koreanName}</td>
                <td
                  style={{
                    color: getCurrentPriceColor(coin.changeRate),
                  }}
                >
                  {coin.currentPrice}
                </td>
                <td style={{ color: getChangeRateColor(coin.changeRate) }}>
                  {coin.changeRate}%
                </td>
                <td>{formatTradeVolume(coin.tradeVolume)}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Table;
