import "./List.css";
import TodoItem from "./TodoItem";
import { useState, useMemo, useContext } from "react";
import { TodoStateContext } from "../App";
const List = () => {
  const todos = useContext(TodoStateContext);
  const [search, setSearch] = useState("");

  const onChangeSearch = (e) => {
    setSearch(e.target.value);
  };

  const getFilterData = () => {
    if (search === "") {
      return todos;
    }
    return todos.filter((todo) =>
      todo.content.toLowerCase().includes(search.toLowerCase())
    );
  };

  const filterTodos = getFilterData();

  const { totalCount, doneCount, notDoneCount } = useMemo(() => {
    console.log("getAnallyzeDate 호출 !");
    // 검색어를 입력해도 함수가 호출이된다.
    // 수정 삭제 추가 되었을때만 함수가 호출이 되어야한다.
    const totalCount = todos.length;
    const doneCount = todos.filter((todo) => todo.isDone).length;

    const notDoneCount = totalCount - doneCount;

    return {
      totalCount,
      doneCount,
      notDoneCount,
    };
  }, [todos]);
  // 의존성 배열 : deps

  // const { totalCount, doneCount, notDoneCount } = getAnalyzeData();

  return (
    <div className="List">
      <h4>Todo List🎃</h4>
      <div>
        <div>total : {totalCount}</div>
        <div>Done : {doneCount}</div>
        <div>notDone : {notDoneCount}</div>
      </div>
      <input
        value={search}
        onChange={onChangeSearch}
        placeholder="검색어를 입력하세요."
      />
      <div className="todos_wrapper">
        {filterTodos.map((todo) => {
          return <TodoItem key={todo.id} {...todo} />;
        })}
      </div>
    </div>
  );
};

export default List;
