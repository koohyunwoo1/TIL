// 검색 함수

import { useState, useEffect } from "react";

const useSearch = (coinData, searchKey = "koreanName") => {
  const [searchTerm, setSearchTerm] = useState("");
  const [filteredData, setFilteredData] = useState(coinData);

  const handleSearch = () => {
    if (searchTerm.trim() === "") {
      setFilteredData(coinData);
    } else {
      const filtered = coinData.filter((coin) =>
        coin[searchKey].includes(searchTerm.trim())
      );
      setFilteredData(filtered);
    }
  };

  useEffect(() => {
    handleSearch();
  }, [searchTerm, coinData]);

  return {
    searchTerm,
    setSearchTerm,
    filteredData,
  };
};

export default useSearch;
