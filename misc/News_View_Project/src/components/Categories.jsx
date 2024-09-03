// src/components/Categories.jsx
import React from "react";
import "./Categories.css";

const categories = [
  { name: "all", text: "All" },
  { name: "business", text: "Business" },
  { name: "entertainment", text: "Entertainment" },
  { name: "health", text: "Health" },
  { name: "science", text: "Science" },
  { name: "sports", text: "Sports" },
  { name: "technology", text: "Technology" },
];

function Categories({ onSelect, selectedCategory }) {
  return (
    <div className="categories">
      {categories.map((category) => (
        <div
          key={category.name}
          className={`category ${
            selectedCategory === category.name ? "active" : ""
          }`}
          onClick={() => onSelect(category.name)}
        >
          {category.text}
        </div>
      ))}
    </div>
  );
}

export default Categories;
