<template>
  <div class="login-container">
    <h2>用户登录</h2>
    <form @submit.prevent="handleLogin">
      <div class="form-item">
        <label class="form-label">用户名：</label>
        <input v-model="username" type="text" required class="form-input" />
      </div>
      <div class="form-item">
        <label class="form-label">密 码：</label>
        <input v-model="password" type="password" required class="form-input" />
      </div>
      <button type="submit" class="login-btn">登录</button>
    </form>
    <div v-if="errorMsg" class="error">{{ errorMsg }}</div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import request from "../utils/request";
import { useRouter, useRoute } from "vue-router";
import bus from "../utils/bus"; // 导入事件总线

const router = useRouter();
const route = useRoute();
const username = ref("");
const password = ref("");
const errorMsg = ref("");

const handleLogin = async () => {
  try {
    // 构造form-data格式（匹配后端OAuth2PasswordRequestForm）
    const formData = new FormData();
    formData.append("username", username.value);
    formData.append("password", password.value);

    const res = await request.post("/api/v1/users/token", formData);
    localStorage.setItem("access_token", res.data.access_token);
    // 登录成功后，触发刷新登录态事件
    bus.emit("refresh-menu");
    const redirect = route.query.redirect || "/";
    router.push(redirect); // 登录成功跳转到首页
  } catch (err) {
    errorMsg.value = err.response?.data?.detail || "登录失败，请检查账号密码";
  }
};
</script>

<style scoped>
.login-container {
  width: 400px;
  margin: 50px auto;
  padding: 20px;
  border: 1px solid #e6e6e6;
  border-radius: 8px;
  background: #fff;
}

.login-container h2 {
  text-align: center;
  margin-bottom: 20px;
  color: #333;
}

/* 表单项：弹性布局，让标签和输入框横向排列 */
.form-item {
  display: flex;
  align-items: center; /* 垂直居中对齐 */
  margin-bottom: 15px;
  height: 40px;
}

/* 标签：固定宽度 + 右对齐，确保输入框起点一致 */
.form-label {
  width: 80px; /* 固定宽度，可根据需要调整 */
  text-align: right; /* 文字右对齐，视觉更整齐 */
  padding-right: 10px; /* 标签和输入框之间留间距 */
  font-size: 14px;
  color: #666;
}

/* 输入框：统一宽度 + 样式，确保视觉一致 */
.form-input {
  flex: 1; /* 占满剩余宽度 */
  height: 32px;
  padding: 0 10px;
  border: 1px solid #dcdcdc;
  border-radius: 4px;
  font-size: 14px;
  box-sizing: border-box; /* 避免 padding 撑大宽度 */
}

.form-input:focus {
  outline: none;
  border-color: #409eff; /* 聚焦时高亮边框，提升体验 */
}

/* 登录按钮：宽度适配 + 样式优化 */
.login-btn {
  /* width: calc(100% - 80px); 和输入框宽度对齐 */
  margin-left: 90px; /* 标签宽度 + 间距，和输入框对齐 */
  height: 36px;
  background: #409eff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
}

.login-btn:hover {
  background: #66b1ff; /*  hover 效果 */
}

/* 错误提示 */
.error {
  margin-top: 10px;
  padding-left: 90px; /* 和输入框对齐 */
  color: #f56c6c;
  font-size: 12px;
}
</style>
