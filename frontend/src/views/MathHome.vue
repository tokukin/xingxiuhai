<script setup lang="ts">
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
      <div class="box_math">
        <p>
          <el-tag type="primary" class="text-info">定义</el-tag>
          <el-text class="text-info"
            >数学，是研究数量、结构以及空间等概念及其变化的一门学科，属于形式科学的一种。数学利用抽象化和逻辑推理，从计数、计算、量度、对物体形状及运动的观察发展而成。数学家们拓展这些概念，以公式化新的猜想，以及从选定的公理及定义出发，严谨地推导出一些定理。</el-text
          >
        </p>
      </div>
    </el-col>
    <el-col
      :xs="gridSize"
      :sm="gridSize"
      :md="gridSize"
      :lg="gridSize"
      :xl="gridSize"
    >
      <div class="box_math">
        数学工具
        <!-- 纯图片点击跳转（去掉el-button，响应不变） -->
        <el-button type="primary" @click="handleSelect('/math/calculator')"
          >口算天天练</el-button
        >
      </div>
    </el-col>
    <el-col
      :xs="gridSize"
      :sm="gridSize"
      :md="gridSize"
      :lg="gridSize"
      :xl="gridSize"
    >
      <div class="box_math"></div>
    </el-col>
  </el-row>
</template>

<style>
.box_math {
  height: 30vh;
  background-color: aliceblue;
  font-weight: bold;
  display: flex;
  flex-direction: column;
  justify-content: center; /* 垂直方向居中（主轴居中） */
  align-items: center; /* 水平方向居中（交叉轴居中） */
  padding: 10px;
}

.box_math p {
  text-align: left;
  font-size: 15px;
}
.text-info {
  font-size: 15px;
}
</style>
