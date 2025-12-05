import { defineConfig, loadEnv } from "vite";
import vue from "@vitejs/plugin-vue";
import path from "path";

/*
 * 前端环境变量配置
 * 代理解决跨域问题
 */
// https://vite.dev/config/
export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd());
  return {
    plugins: [vue()],
    server: {
      host: "127.0.0.1",
      port: 5173,
      proxy: {
        "/api": {
          target: env.VITE_API_BASE_URL.replace("/api", ""),
          changeOrigin: true,
          rewrite: (path) => path.replace(/^\/api/, "/api"),
        },
      },
    },
    resolve: {
      alias: {
        // 确保这行配置存在（如果没有则添加）
        "@": path.resolve(__dirname, "./src"),
      },
    },
  };
});

/**
 * 环境变量配置
 * export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd())
  return {
    plugins: [vue()],
    // 开发服务器（代理解决跨域）
    server: {
      host: "127.0.0.1",
      port: 5173,
      proxy: {
        '/api': {
          target: env.VITE_API_BASE_URL.replace('/api', ''),
          changeOrigin: true,
          rewrite: (path) => path.replace(/^\/api/, '/api')
        }
      }
    }
  }
})
 */
