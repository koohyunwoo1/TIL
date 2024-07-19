import React, { useState } from "react";
import "../../styles/Common/Button.css";
const FindEmailModalContent = ({ onClose }) => {
  const [email, setEmail] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    // Add logic to handle email submission
    console.log("Email submitted:", email);
    onClose();
  };

  return (
    <div>
      <h2>비밀번호</h2>
      <form onSubmit={handleSubmit}>
        <label htmlFor="email">이메일을 입력해주세요:</label>
        <input
          type="email"
          id="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <button type="submit" className="Button">
          제출
        </button>
      </form>
    </div>
  );
};

export default FindEmailModalContent;
