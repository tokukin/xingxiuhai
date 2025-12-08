// src/utils/request.js
import axios from "axios";
import router from "@/router"; // 导入路由实例，替代 window.location.href

const request = axios.create({
  baseURL: "http://localhost:8001",
  timeout: 5000,
  withCredentials: true,
});

// 请求拦截器
request.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem("access_token");
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// 响应拦截器（修复循环跳转）
request.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem("access_token");
      // 关键：判断当前页面是否已是登录页，避免重复跳转
      const currentPath = router.currentRoute.path;
      if (currentPath !== "/user/login") {
        // 用 Vue Router 跳转，而非 window.location.href（避免页面刷新）
        router.push("/user/login");
      }
    }
    return Promise.reject(error);
  }
);

export default request;
