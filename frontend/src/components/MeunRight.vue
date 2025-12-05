<script setup>
import { ref } from "vue";
import { useRouter, useRoute } from "vue-router";

const router = useRouter();
const route = useRoute();

const activeIndex = route.path;
const handleSelect = (index) => {
  // index 即 el-menu-item 的 index 属性值（路由路径）
  router.push(index); // 跳转到对应路由
};

// 导入路由 hooks（Vue 3）
// Vue 2 中使用：import { $router, $route } from 'vue'
</script>
<template>
  <el-menu
    :default-active="activeIndex"
    class="el-menu-demo"
    mode="horizontal"
    :ellipsis="false"
    @select="handleSelect"
  >
    <el-menu-item index="/">
      <img style="width: 50px" src="../assets/logo.svg" alt="Element logo" ><div style="font-size: 35px;font-weight: bold;">星宿海</div></img>
    </el-menu-item>
    <!-- <el-menu-item index="/">首页</el-menu-item> -->
    <el-menu-item index="/math">数学</el-menu-item>
    <el-menu-item index="/physics">物理</el-menu-item>
    <el-menu-item index="/chemistry">化学</el-menu-item>
  </el-menu>
</template>
<style>
.el-menu .el-menu-item {
  font-size: 20px; /* 覆盖菜单项字体 */
}
.el-menu .el-sub-menu__title {
  font-size: 20px; /* 更简洁的选择器，确保应用到所有子菜单标题 */
}
.el-header {
  width: 100%;
  height: 60px;

  padding: 0;
}
.el-menu--horizontal {
  --el-menu-horizontal-height: 70px;
}
.el-menu--horizontal > .el-menu-item:nth-child(1) {
  margin-right: auto;
}
</style>
