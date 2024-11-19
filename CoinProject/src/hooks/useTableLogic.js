// 정렬 함수 / 색상 함수

import { useState, useEffect } from "react";

const useTableLogic = (coinData) => {
  const [sortedData, setSortedData] = useState([]);
  const [sortKey, setSortKey] = useState("");
  const [sortOrder, setSortOrder] = useState("asc");

  const handleSort = (key) => {
    const newOrder = sortKey === key && sortOrder === "asc" ? "desc" : "asc";
    setSortKey(key);
    setSortOrder(newOrder);

    const sorted = [...sortedData].sort((a, b) => {
      if (key === "koreanName") {
        return newOrder === "asc"
          ? a[key].localeCompare(b[key])
          : b[key].localeCompare(a[key]);
      }
      if (key === "currentPrice" || key === "tradeVolume") {
        const aNum = parseFloat(a[key].replace(/,/g, ""));
        const bNum = parseFloat(b[key].replace(/,/g, ""));
        return newOrder === "asc" ? aNum - bNum : bNum - aNum;
      }
      if (key === "changeRate") {
        return newOrder === "asc"
          ? parseFloat(a[key]) - parseFloat(b[key])
          : parseFloat(b[key]) - parseFloat(a[key]);
      }
      return 0;
    });

    setSortedData(sorted);
  };

  useEffect(() => {
    let sorted = [...coinData];
    if (sortKey) {
      sorted = sorted.sort((a, b) => {
        if (sortKey === "koreanName") {
          return sortOrder === "asc"
            ? a[sortKey].localeCompare(b[sortKey])
            : b[sortKey].localeCompare(a[sortKey]);
        }
        if (sortKey === "currentPrice" || sortKey === "tradeVolume") {
          const aNum = parseFloat(a[sortKey].replace(/,/g, ""));
          const bNum = parseFloat(b[sortKey].replace(/,/g, ""));
          return sortOrder === "asc" ? aNum - bNum : bNum - aNum;
        }
        if (sortKey === "changeRate") {
          return sortOrder === "asc"
            ? parseFloat(a[sortKey]) - parseFloat(b[sortKey])
            : parseFloat(b[sortKey]) - parseFloat(a[sortKey]);
        }
        return 0;
      });
    }
    setSortedData(sorted);
  }, [coinData, sortKey, sortOrder]);

  const getChangeRateColor = (changeRate) => {
    const rate = parseFloat(changeRate);
    if (rate > 0) return "red";
    if (rate < 0) return "blue";
    return "black";
  };

  const getCurrentPriceColor = (changeRate) => {
    const rate = parseFloat(changeRate);
    if (rate > 0) return "red";
    if (rate < 0) return "blue";
    return "black";
  };

  const formatTradeVolume = (tradeVolume) => {
    return String(tradeVolume).replace(/(\d)(?=(?:\d{3})+(?!\d))/g, "$1,");
  };

  return {
    sortedData,
    handleSort,
    getChangeRateColor,
    getCurrentPriceColor,
    formatTradeVolume,
  };
};

export default useTableLogic;
