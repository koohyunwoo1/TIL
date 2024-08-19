import React, { useState, useEffect, useRef } from "react";

function App() {
  // 현재 위치 상태 저장할 상태 변수
  const [location, setLocation] = useState({ latitude: null, longitude: null });
  // 이동 거리 저장할 상태 변수
  const [distance, setDistance] = useState(0);
  // 에러 메시지 저장할 상태 변수
  const [error, setError] = useState(null);
  // 이전 위치 정보를 저장할 ref 변수
  const prevLocation = useRef({
    latitude: null,
    longitude: null,
    timestamp: null,
    speed: null,
  });

  useEffect(() => {
    // 브라우저에서 지리적 위치 정보 제공 안 하면 에러 처리
    if (!navigator.geolocation) {
      setError("Geolocation is not supported by your browser");
      return;
    }

    // 위치 정보 얻기 성공했을 때 처리 함수
    const handleSuccess = (position) => {
      // 현재 위치 정보에서 위도, 경도, 속도 추출
      const { latitude, longitude, speed } = position.coords;
      // 현재 시간 저장
      const currentTime = Date.now();

      // 이전 위치 정보가 있을 때
      if (
        prevLocation.current.latitude !== null &&
        prevLocation.current.longitude !== null
      ) {
        // 경과 시간(초) 계산
        const timeElapsed =
          (currentTime - prevLocation.current.timestamp) / 1000;
        // 최대 이동 가능 거리 계산 (속도 * 경과 시간)
        const maxPossibleDistance =
          (prevLocation.current.speed || 0) * timeElapsed;
        // 이전 위치와 현재 위치 간의 거리 계산
        const dist = calculateDistance(
          prevLocation.current.latitude,
          prevLocation.current.longitude,
          latitude,
          longitude
        );

        // 현재 위치가 최대 이동 가능 거리를 넘어가는 경우 보정
        if (dist > maxPossibleDistance) {
          // 보정된 위치 계산
          const correctedLocation = correctLocation(
            prevLocation.current.latitude,
            prevLocation.current.longitude,
            latitude,
            longitude,
            maxPossibleDistance
          );
          // 이동 거리 업데이트 (보정된 최대 이동 거리 더함)
          setDistance((prevDistance) => prevDistance + maxPossibleDistance);
          // 이전 위치 정보 업데이트 (보정된 위치와 현재 시간, 속도)
          prevLocation.current = {
            ...correctedLocation,
            timestamp: currentTime,
            speed,
          };
          // 현재 위치 업데이트 (보정된 위치)
          setLocation(correctedLocation);
        } else {
          // 정상적인 경우 위치 정보 업데이트
          setDistance((prevDistance) => prevDistance + dist);
          prevLocation.current = {
            latitude,
            longitude,
            timestamp: currentTime,
            speed,
          };
          setLocation({ latitude, longitude });
        }
      } else {
        // 초기 위치 설정
        prevLocation.current = {
          latitude,
          longitude,
          timestamp: currentTime,
          speed,
        };
        setLocation({ latitude, longitude });
      }
    };

    // 위치 정보 얻기 실패했을 때 처리 함수
    const handleError = (error) => {
      setError(error.message);
    };

    const options = {
      enableHighAccuracy: true, // 높은 정확도의 위치 정보 요청
      maximumAge: 0, // 캐시된 위치 정보 사용 안 함
    };

    // 초기 위치 업데이트
    navigator.geolocation.getCurrentPosition(
      handleSuccess,
      handleError,
      options
    );

    // 위치 변화 모니터링
    const watchId = navigator.geolocation.watchPosition(
      handleSuccess,
      handleError,
      options
    );

    // 컴포넌트 언마운트 시 위치 모니터링 정지
    return () => navigator.geolocation.clearWatch(watchId);
  }, []);

  // 두 지점 간의 거리 계산 함수 (Haversine formula 사용)
  const calculateDistance = (lat1, lon1, lat2, lon2) => {
    const R = 6371e3; // 지구 반경 (미터 단위)
    const rad = Math.PI / 180; // 라디안 변환 상수
    const φ1 = lat1 * rad; // 위도1 라디안 변환
    const φ2 = lat2 * rad; // 위도2 라디안 변환
    const Δφ = (lat2 - lat1) * rad; // 위도 차이 라디안 변환
    const Δλ = (lon2 - lon1) * rad; // 경도 차이 라디안 변환

    // Haversine formula 적용
    const a =
      Math.sin(Δφ / 2) * Math.sin(Δφ / 2) +
      Math.cos(φ1) * Math.cos(φ2) * Math.sin(Δλ / 2) * Math.sin(Δλ / 2);
    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

    return R * c; // 거리 반환 (미터 단위)
  };

  // 위치 보정 함수
  const correctLocation = (lat1, lon1, lat2, lon2, maxDist) => {
    const dist = calculateDistance(lat1, lon1, lat2, lon2);
    const ratio = maxDist / dist; // 최대 이동 거리 대비 실제 거리 비율 계산
    const correctedLat = lat1 + (lat2 - lat1) * ratio; // 보정된 위도 계산
    const correctedLon = lon1 + (lon2 - lon1) * ratio; // 보정된 경도 계산
    return { latitude: correctedLat, longitude: correctedLon };
  };

  return (
    <div style={{ textAlign: "center", padding: "20px" }}>
      <h1>Geolocation Tracker</h1>
      {error ? (
        // 에러 메시지 표시
        <p>Error: {error}</p>
      ) : (
        <>
          {/* 현재 위치와 이동 거리 표시 */}
          <p>Latitude: {location.latitude}</p>
          <p>Longitude: {location.longitude}</p>
          <p>Distance traveled: {distance.toFixed(2)} meters</p>
        </>
      )}
    </div>
  );
}

export default App;
