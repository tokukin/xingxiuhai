<script setup lang="ts">
import { MoreFilled } from "@element-plus/icons-vue";
import { StarFilled } from "@element-plus/icons-vue";

import { ref } from "vue";
import { off } from "node:process";
import { useRouter } from "vue-router";

const router = useRouter();

// 接收路由路径参数，实现跳转
const handleSelect = (path: string) => {
  console.log("跳转路径：", path);
  router.push(path); // 跳转到传入的路由路径
};
const gutterSize = ref(2);
const gridSize = ref(8);

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
      <div class="box"></div>
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
