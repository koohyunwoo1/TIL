// src/components/SocialKakao.jsx
import React from "react";
import kakao from "../assets/kakao.png";
const SocialKakao = () => {
  const RestApiKey = "";
  const redirectUrl = "";

  const kakaoUrl = `https://kauth.kakao.com/oauth/authorize?client_id=${RestApiKey}&redirect_uri=${redirectUrl}&response_type=code`;
  const code = new URL(window.location.href).searchParams.get("code");
  console.log(code);
  // 이 코드를 백엔드로 넘겨주면 끝
  const handleLogin = () => {
    window.location.href = kakaoUrl;
  };

  return (
    <>
      <button onClick={handleLogin}>
        <img src={kakao} />
      </button>
    </>
  );
};

export default SocialKakao;
