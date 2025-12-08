<script setup lang="ts">
import { MoreFilled } from "@element-plus/icons-vue";
import { StarFilled } from "@element-plus/icons-vue";

import { ref, onMounted, onUnmounted } from "vue";
import { off } from "node:process";
import { useRouter } from "vue-router";
import request from "../utils/request";
import bus from "../utils/bus"; // 导入事件总线

const router = useRouter();
const userInfo = ref(null);

// 接收路由路径参数，实现跳转
const handleSelect = (path: string) => {
  console.log("跳转路径：", path);
  router.push(path); // 跳转到传入的路由路径
};
const gutterSize = ref(2);
const gridSize = ref(8);

// 退出登录
const logout = () => {
  localStorage.removeItem("access_token");
  userInfo.value = null;
  bus.emit("delete-user-info");
  router.push("/");
};

// 获取当前用户信息
const fetchUserInfo = async () => {
  try {
    const res = await request.get("/api/v1/users/me/");
    userInfo.value = res.data;
  } catch (err) {
    console.error("获取用户信息失败", err);
  }
};

const activities = [
  {
    content:
      "2025年12月8日完成项目初始化，完成数学：口算，化学：元素周期表开发。",
    timestamp: "2025年12月8日",
    size: "large",
    type: "primary",
    icon: MoreFilled,
  },
  {
    content: "Custom color",
    timestamp: "2018-04-03 20:46",
    color: "#0bbd87",
  },
  {
    content: "Custom size",
    timestamp: "2018-04-03 20:46",
    size: "large",
  },
  {
    content: "Custom hollow",
    timestamp: "2018-04-03 20:46",
    type: "primary",
    hollow: true,
  },
  {
    content: "Default node",
    timestamp: "2018-04-03 20:46",
  },
];
const delUserInfo = () => {
  userInfo.value = null;
};
bus.on("delete-user-info", delUserInfo);
onMounted(() => {
  if (localStorage.getItem("access_token")) {
    fetchUserInfo();
  }
});
onUnmounted(() => {
  bus.off("refresh-menu", fetchUserInfo);
});
onUnmounted(() => {
  bus.off("delete-user-info", delUserInfo);
});
</script>

<template>
  <el-row :gutter="gutterSize">
    <el-col
      :xs="gridSize"
      :sm="gridSize"
      :md="gridSize"
      :lg="gridSize"
      :xl="gridSize"
    >
      <div class="box"></div>
    </el-col>
    <el-col
      :xs="gridSize"
      :sm="gridSize"
      :md="gridSize"
      :lg="gridSize"
      :xl="gridSize"
    >
      <div class="box">
        <div>
          <span>欢迎使用学习系统. </span>
          <el-divider content-position="left">加油！！加油！！</el-divider>
          <span> 系统逐步开发中 </span>
          <el-divider>
            <el-icon><star-filled /></el-icon>
          </el-divider>
          <span>现有功能：数学口算，化学元素周期表。</span>
        </div>
      </div>
    </el-col>
    <el-col
      :xs="gridSize"
      :sm="gridSize"
      :md="gridSize"
      :lg="gridSize"
      :xl="gridSize"
    >
      <div class="box">
        <div>
          <h2>登录</h2>
          <div v-if="userInfo">
            <p>当前登录用户：{{ userInfo.username }}</p>
            <p>邮箱：{{ userInfo.email }}</p>
            <el-button type="primary" @click="logout">退出登录</el-button>
          </div>
          <div v-else>
            <p>未登录，请<router-link to="/user/login">登录</router-link></p>
          </div>
        </div>
      </div>
    </el-col>
  </el-row>
  <el-row> </el-row>
</template>

<style>
.box {
  height: 70vh;
  background-color: aliceblue;
  font-weight: bold;
  display: flex;
  flex-direction: column;
  justify-content: center; /* 垂直方向居中（主轴居中） */
  align-items: center; /* 水平方向居中（交叉轴居中） */
  padding: 10px;
}

.box p {
  text-align: left;
  font-size: 15px;
}
.text-info {
  font-size: 15px;
}
</style>
