import React, { useState } from "react";

const FindPhoneNumberModalContent = ({ onClose }) => {
  const [phoneNumber, setPhoneNumber] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    // Add logic to handle phone number submission
    console.log("Phone number submitted:", phoneNumber);
    onClose();
  };

  return (
    <div>
      <h2>이메일 찾기</h2>
      <form onSubmit={handleSubmit}>
        <label htmlFor="phone">휴대폰 번호를 입력해주세요:</label>
        <input
          type="tel"
          id="phone"
          value={phoneNumber}
          onChange={(e) => setPhoneNumber(e.target.value)}
          required
        />
        <button type="submit" className="Button">
          제출
        </button>
      </form>
    </div>
  );
};

export default FindPhoneNumberModalContent;
