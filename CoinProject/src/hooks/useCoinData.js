// API 호출 함수

import { useState, useEffect } from "react";

const useCoinData = () => {
  const [coinData, setCoinData] = useState([]);
  const [error, setError] = useState(null);

  const formatNumber = (num) => {
    return String(num).replace(/(\d)(?=(?:\d{3})+(?!\d))/g, "$1,");
  };

  const fetchCoinData = async () => {
    try {
      const marketsResponse = await fetch(
        "https://api.upbit.com/v1/market/all"
      );
      if (!marketsResponse.ok) throw new Error("마켓 코드 조회 실패");

      const markets = await marketsResponse.json();
      const krwMarkets = markets.filter((market) =>
        market.market.startsWith("KRW-")
      );
      const marketCodes = krwMarkets.map((market) => market.market).join(",");
      const koreanNames = krwMarkets.map((market) => market.korean_name);

      const tickerResponse = await fetch(
        `https://api.upbit.com/v1/ticker?markets=${marketCodes}`
      );
      if (!tickerResponse.ok) throw new Error("시세 정보 조회 실패");
      const tickers = await tickerResponse.json();
      console.log(tickers);
      const combinedData = tickers.map((ticker, index) => ({
        koreanName: koreanNames[index],
        currentPrice: formatNumber(ticker.trade_price),
        changeRate: (ticker.signed_change_rate * 100).toFixed(2),
        tradeVolume:
          ticker.acc_trade_price_24h > 1000000
            ? `${(ticker.acc_trade_price_24h / 1000000).toFixed(0)}백만`
            : `${ticker.acc_trade_price_24h.toFixed(0)}`,
      }));
      setCoinData(combinedData);
    } catch (err) {
      setError(err.message);
    }
  };

  useEffect(() => {
    fetchCoinData();
    const interval = setInterval(fetchCoinData, 1000);
    return () => clearInterval(interval);
  }, []);

  return { coinData, error };
};

export default useCoinData;
