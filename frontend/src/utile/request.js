// src/utils/request.js
import axios from "axios";

// 根据环境自动选择 API 基础路径
const getBaseURL = () => {
  // 开发环境：从环境变量读取
  if (import.meta.env.DEV) {
    return import.meta.env.VITE_API_BASE_URL || "http://localhost:3000/api";
  }
  // 生产环境：使用相对路径（由 Nginx 代理）
  return "/api";
};

const request = axios.create({
  baseURL: getBaseURL(),
  timeout: 10000,
  headers: {
    "Content-Type": "application/json",
  },
});

// 请求拦截器
request.interceptors.request.use(
  (config) => {
    // 可以在这里添加 token 等
    const token = localStorage.getItem("token");
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// 响应拦截器
request.interceptors.response.use(
  (response) => {
    return response.data;
  },
  (error) => {
    // 统一错误处理
    console.error("API Error:", error);
    return Promise.reject(error);
  }
);

export default request;
