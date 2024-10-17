import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  optimizeDeps: {
    include: ["react-icons/fa", "react-icons/si"], // 사용 중인 react-icons 경로 추가
  },
});
