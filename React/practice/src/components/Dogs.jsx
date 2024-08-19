// 무한 스크롤
// npm install axios
import React, { useEffect, useState, useRef, useCallback } from "react";
import axios from "axios";

export default function Dogs() {
  const [dogImgArr, setDogImgArr] = useState([]);
  const [page, setPage] = useState(0);
  const [loading, setLoading] = useState(false);
  const observer = useRef();

  const fetchDogs = async () => {
    setLoading(true);
    const API_URL = `https://api.thedogapi.com/v1/images/search?size=small&format=json&has_breeds=true&order=ASC&page=${page}&limit=10`;
    const res = await axios.get(API_URL);
    const gotData = res.data.map((dogImg) => ({
      id: dogImg.id,
      dogUrl: dogImg.url,
    }));
    setDogImgArr((prev) => [...prev, ...gotData]);
    setLoading(false);
  };

  useEffect(() => {
    fetchDogs();
  }, [page]);

  const lastDogElementRef = useCallback(
    (node) => {
      if (loading) return;
      if (observer.current) observer.current.disconnect();
      observer.current = new IntersectionObserver((entries) => {
        if (entries[0].isIntersecting) {
          setPage((prev) => prev + 1);
        }
      });
      if (node) observer.current.observe(node);
    },
    [loading]
  );

  return (
    <div className="dog-imgs-container">
      {dogImgArr.map((dogImg, index) => (
        <div
          key={dogImg.id}
          className="dog-img-card"
          ref={index === dogImgArr.length - 1 ? lastDogElementRef : null}
        >
          <img src={dogImg.dogUrl} alt={`cute_${dogImg.id}`} />
          <p>cute_{dogImg.id}</p>
        </div>
      ))}
      {loading && <p>Loading...</p>}
    </div>
  );
}
