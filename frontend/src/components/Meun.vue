<script setup lang="ts">
import { ref } from "vue";
import { useRouter, useRoute } from "vue-router";

const router = useRouter();
const route = useRoute();

const activeIndex2 = route.path;
const handleSelect = (index: string) => {
  // index 即 el-menu-item 的 index 属性值（路由路径）
  router.push(index); // 跳转到对应路由
};

// 导入路由 hooks（Vue 3）
// Vue 2 中使用：import { $router, $route } from 'vue'
</script>
<template>
  <el-menu
    :default-active="activeIndex2"
    class="el-menu-demo"
    mode="horizontal"
    @select="handleSelect"
  >
    <el-menu-item index="/">首页</el-menu-item>
    <el-menu-item index="/math">数学</el-menu-item>
    <!-- <el-sub-menu index="2">
      <template #title>数学</template>
      <el-menu-item index="2-1">代数</el-menu-item>
      <el-menu-item index="2-2">几何</el-menu-item>
    </el-sub-menu> -->
    <el-menu-item index="/physics">物理</el-menu-item>
    <el-menu-item index="/chemistry">化学</el-menu-item>
  </el-menu>
</template>
<style>
.el-menu .el-menu-item {
  font-size: 25px; /* 覆盖菜单项字体 */
}
.el-menu .el-sub-menu__title {
  font-size: 25px; /* 更简洁的选择器，确保应用到所有子菜单标题 */
}
.el-header {
  width: 100%;
  height: 60px;

  padding: 0;
}
.el-menu--horizontal {
  --el-menu-horizontal-height: 80px;
}
</style>
