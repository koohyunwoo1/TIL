// src/components/NewsList.jsx
import React, { useEffect, useState, useRef } from "react";
import axios from "axios";
import NewsItem from "./NewsItem";
import "./NewsList.css";

function NewsList({ category }) {
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(false);
  const listRef = useRef(null);

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      try {
        const response = await axios.get(
          `https://newsapi.org/v2/everything?q=tesla&from=2024-06-05&sortBy=publishedAt&apiKey=02c8e06e4bc644938a8b44316bbfdbc5`
        );
        setArticles(response.data.articles);
      } catch (error) {
        console.error(error);
      }
      setLoading(false);
    };
    fetchData();
  }, [category]);

  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries, observer) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("appear");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.1 }
    );

    if (listRef.current) {
      const items = listRef.current.querySelectorAll(".news-item");
      items.forEach((item) => observer.observe(item));

      return () => {
        items.forEach((item) => observer.unobserve(item));
      };
    }
  }, [articles]);

  if (loading) {
    return <div className="news-list">Loading...</div>;
  }

  if (!articles.length) {
    return <div className="news-list">No articles found.</div>;
  }

  return (
    <>
      <div className="news">
        <h4>Tesla뉴스 소식</h4>
        <div className="news-list" ref={listRef}>
          {articles.map((article) => (
            <NewsItem key={article.url} article={article} />
          ))}
        </div>
      </div>
    </>
  );
}

export default NewsList;
