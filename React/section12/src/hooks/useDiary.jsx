// 재사용성으로 인해 hooks폴더에 따로 분리

import { useContext, useState, useEffect } from "react";
import { DiaryStateContext } from "../App";
import { useNavigate } from "react-router-dom";

const useDiary = (id) => {
  const data = useContext(DiaryStateContext);
  const [curDiaryItem, setCurDiaryItem] = useState();
  const nav = useNavigate();

  useEffect(() => {
    const currentDiaryItme = data.find(
      (item) => String(item.id) === String(id)
    );
    if (!currentDiaryItme) {
      window.alert("존재하지 않는 일기입니다.");
      nav("/", { replace: true });
      // replace : true는 사용자가 뒤로가기 버튼을 눌러도
      // 뒤로 돌아가지 못하게 막아준다.
    }

    setCurDiaryItem(currentDiaryItme);
  }, [id, data]);
  // id, data가 변경될때마다 useEffect 훅이 실행이 됨

  return curDiaryItem;
};

export default useDiary;
// useDiary는 주어진 id에 해당하는 일기 항목을 찾고, 일기 항목이
// 존재하지 않으면 사용자에게 알리고 홈으로 리디렉션하는 역할
