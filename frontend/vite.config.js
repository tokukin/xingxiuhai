import { defineConfig, loadEnv } from "vite";
import vue from "@vitejs/plugin-vue";
import path from "path";

// 获取环境模式
const mode = process.env.NODE_ENV || "development";

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), "");

  // 判断当前环境
  const isProduction = mode === "production";

  return {
    plugins: [vue()],

    // 开发环境配置
    server: {
      host: "127.0.0.1",
      port: 5173,
      // 开发环境：使用 Vite 代理
      proxy: isProduction
        ? undefined
        : {
            // 代理 API 请求
            "/api": {
              target:
                env.VITE_API_BASE_URL?.replace("/api", "") ||
                "http://localhost:3000",
              changeOrigin: true,
              secure: false,
              // 可根据需要重写路径
              rewrite: (path) => {
                // 如果你的后端 API 路径需要调整，可以在这里处理
                // 例如：将 /api/users 重写为 /users
                return path;
              },
            },

            // 可以添加更多代理规则
            "/uploads": {
              target:
                env.VITE_API_BASE_URL?.replace("/api", "") ||
                "http://localhost:3000",
              changeOrigin: true,
              secure: false,
            },
          },

      // 开发环境热更新
      hmr: {
        overlay: true,
      },
    },

    resolve: {
      alias: {
        "@": path.resolve(__dirname, "./src"),
      },
    },

    // 生产环境构建配置
    build: {
      outDir: "dist",
      sourcemap: false,
      // 生产环境公共路径
      assetsDir: "assets",
      rollupOptions: {
        output: {
          // 文件命名规则
          chunkFileNames: "assets/js/[name]-[hash].js",
          entryFileNames: "assets/js/[name]-[hash].js",
          assetFileNames: "assets/[ext]/[name]-[hash].[ext]",
        },
      },
    },

    // 环境变量配置
    define: {
      "process.env.NODE_ENV": JSON.stringify(mode),
      "import.meta.env.MODE": JSON.stringify(mode),
    },
  };
});
