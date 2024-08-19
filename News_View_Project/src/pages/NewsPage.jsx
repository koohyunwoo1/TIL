// src/pages/NewsPage.jsx
import React, { useState } from "react";
import Categories from "../components/Categories";
import NewsList from "../components/NewsList";

function NewsPage() {
  const [category, setCategory] = useState("all");

  const handleSelectCategory = (category) => {
    setCategory(category);
  };

  return (
    <div>
      <Categories onSelect={handleSelectCategory} selectedCategory={category} />
      <NewsList category={category} />
    </div>
  );
}

export default NewsPage;
