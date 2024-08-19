import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
    <App />
    // 관례상 App컴포넌트를 조상 컴포넌트로 가지기 때문에 App으로 설정하자.
);
