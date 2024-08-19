import { useEffect } from "react";

const usePageTite = (title) => {
  useEffect(() => {
    const $title = document.getElementsByTagName("title")[0];
    // title 태그가 하나만 존재하기 때문에
    // [0]을 사용하여 첫번째 요소를 선택해서 가져온다
    $title.innerText = title;
  }, [title]);
  // 의존성배열 [title]을 이용해서
  // title이 변경될때마다 useEffect훅을 다시 실행하게 된다.
};

export default usePageTite;
