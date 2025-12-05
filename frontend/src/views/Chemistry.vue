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
      <div class="box">
        <p>
          <el-tag type="primary" class="text-info">定义</el-tag>
          <el-text class="text-info"
            >化学是研究物质的组成、结构、性质、转化及应用的一门基础学科，其特征是从分子层次认识物质，通过化学变化创造物质。</el-text
          >
        </p>
        <p>
          <el-tag type="success" class="text-info">特征</el-tag>
          <el-text class="text-info"
            >化学变化的特征是有<el-text class="text-info" type="danger"
              >新物质生成</el-text
            >，常表现为改变颜色、放出气体、生成沉淀等。化学变化不但生成新物质，而且伴随着能量的变化，这种能量变化常表现为放热、吸热、发光等。</el-text
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
      <div class="box">
        <!-- 纯图片点击跳转（去掉el-button，响应不变） -->
        <a
          @click="handleSelect('/chemistry/periodic-table')"
          style="cursor: pointer; display: inline-block"
        >
          <img
            src="../assets/hxyszqb.png"
            alt="化学元素周期表"
            style="width: 70%; border: none"
          />
        </a>
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
</template>

<style>
.box {
  height: 30vh;
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
  font-size: 20px;
}
.text-info {
  font-size: 20px;
}
</style>
