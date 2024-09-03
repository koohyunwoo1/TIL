// src/components/NewsItem.jsx
import React from "react";
import "./NewsItem.css";

function NewsItem({ article }) {
  const { title, description, url, urlToImage } = article;

  return (
    <div className="news-item">
      {urlToImage && (
        <div className="thumbnail">
          <img src={urlToImage} alt="thumbnail" />
        </div>
      )}
      <div className="contents">
        <h2>
          <a href={url} target="_blank" rel="noopener noreferrer">
            {title}
          </a>
        </h2>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default NewsItem;
