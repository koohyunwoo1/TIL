import React from "react";
import { Routes, Route } from "react-router-dom";
import LogOutHeader from "./pages/Home/LogOutHeader";
import SignIn from "./pages/Auth/SignIn";
import SignUp from "./pages/Auth/SignUp";

const App = () => {
  return (
    <div>
      <LogOutHeader />
      <Routes>
        <Route path="/signin" element={<SignIn />} />
        <Route path="/signup" element={<SignUp />} />
      </Routes>
    </div>
  );
};

export default App;
