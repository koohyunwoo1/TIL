import React from "react";
import { Routes, Route } from "react-router-dom";
import LogOutHeader from "./pages/Home/LogOutHeader";
import SignIn from "./pages/Auth/SignIn";
import SignUp from "./pages/Auth/SignUp";
import LogOutHome from "./pages/Home/LogOutHome";
const App = () => {
  return (
    <div>
      <LogOutHeader />
      <Routes>
        <Route path="/signin" element={<SignIn />} />
        <Route path="/signup" element={<SignUp />} />
        <Route path="/" element={<LogOutHome />} />
      </Routes>
    </div>
  );
};

export default App;
