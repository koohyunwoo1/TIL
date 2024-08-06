import React, { useState, useEffect, useRef } from "react";

function App() {
  const [location, setLocation] = useState({ latitude: null, longitude: null });
  const [distance, setDistance] = useState(0);
  const [error, setError] = useState(null);
  const prevLocation = useRef({
    latitude: null,
    longitude: null,
    timestamp: null,
    speed: null,
  });

  useEffect(() => {
    if (!navigator.geolocation) {
      setError("Geolocation is not supported by your browser");
      return;
    }

    const handleSuccess = (position) => {
      const { latitude, longitude, speed } = position.coords;
      const currentTime = Date.now();

      if (
        prevLocation.current.latitude !== null &&
        prevLocation.current.longitude !== null
      ) {
        const timeElapsed =
          (currentTime - prevLocation.current.timestamp) / 1000; // seconds
        const maxPossibleDistance =
          (prevLocation.current.speed || 0) * timeElapsed; // m/s * s = m
        const dist = calculateDistance(
          prevLocation.current.latitude,
          prevLocation.current.longitude,
          latitude,
          longitude
        );

        if (dist > maxPossibleDistance) {
          // 현재 위치가 최대 이동 가능 거리를 넘어가면 보정
          const correctedLocation = correctLocation(
            prevLocation.current.latitude,
            prevLocation.current.longitude,
            latitude,
            longitude,
            maxPossibleDistance
          );
          setDistance((prevDistance) => prevDistance + maxPossibleDistance);
          prevLocation.current = {
            ...correctedLocation,
            timestamp: currentTime,
            speed,
          };
          setLocation(correctedLocation);
        } else {
          // 정상적인 경우 위치 갱신
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

    const handleError = (error) => {
      setError(error.message);
    };

    const options = {
      enableHighAccuracy: true,
      maximumAge: 0, // Do not use cached location
    };

    // Initial location update
    navigator.geolocation.getCurrentPosition(
      handleSuccess,
      handleError,
      options
    );

    // Monitor location changes
    const watchId = navigator.geolocation.watchPosition(
      handleSuccess,
      handleError,
      options
    );

    return () => navigator.geolocation.clearWatch(watchId);
  }, []);

  const calculateDistance = (lat1, lon1, lat2, lon2) => {
    const R = 6371e3; // Earth's radius in meters
    const rad = Math.PI / 180;
    const φ1 = lat1 * rad;
    const φ2 = lat2 * rad;
    const Δφ = (lat2 - lat1) * rad;
    const Δλ = (lon2 - lon1) * rad;

    const a =
      Math.sin(Δφ / 2) * Math.sin(Δφ / 2) +
      Math.cos(φ1) * Math.cos(φ2) * Math.sin(Δλ / 2) * Math.sin(Δλ / 2);
    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

    return R * c; // Return distance in meters
  };

  const correctLocation = (lat1, lon1, lat2, lon2, maxDist) => {
    const dist = calculateDistance(lat1, lon1, lat2, lon2);
    const ratio = maxDist / dist;
    const correctedLat = lat1 + (lat2 - lat1) * ratio;
    const correctedLon = lon1 + (lon2 - lon1) * ratio;
    return { latitude: correctedLat, longitude: correctedLon };
  };

  return (
    <div style={{ textAlign: "center", padding: "20px" }}>
      <h1>Geolocation Tracker</h1>
      {error ? (
        <p>Error: {error}</p>
      ) : (
        <>
          <p>Latitude: {location.latitude}</p>
          <p>Longitude: {location.longitude}</p>
          <p>Distance traveled: {distance.toFixed(2)} meters</p>
        </>
      )}
    </div>
  );
}

export default App;
