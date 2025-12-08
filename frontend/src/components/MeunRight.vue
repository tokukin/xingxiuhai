<script setup>
import { ref, onMounted, watch, onUnmounted } from "vue";
import { useRouter, useRoute } from "vue-router";
import request from "../utils/request";
import bus from "../utils/bus"; // 导入事件总线

const router = useRouter();
const route = useRoute();
const userInfo = ref(null);
const activeIndex = ref(route.path);
const handleSelect = (index) => {
  // index 即 el-menu-item 的 index 属性值（路由路径）
  router.push(index); // 跳转到对应路由
};
// 退出登录
const logout = () => {
  localStorage.removeItem("access_token");
  userInfo.value = null;
  bus.emit('delete-user-info'); 
  router.push("/");
};

// 获取当前用户信息
const fetchUserInfo = async () => {
  try {
    const res = await request.get("/api/v1/users/me/");
    userInfo.value = res.data;
    console.log("刷新用户信息", userInfo.value);
  } catch (err) {
    console.error("获取用户信息失败", err);
  }
};
const delUserInfo = () => {
  userInfo.value = null;
}
bus.on('refresh-menu', fetchUserInfo);
bus.on('delete-user-info', delUserInfo);



// 3. 组件卸载时移除监听（必做：避免内存泄漏）
onUnmounted(() => {
  bus.off('refresh-menu', fetchUserInfo);
});
onUnmounted(() => {
  bus.off("delete-user-info", delUserInfo);
});

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
      <img style="width: 25px" src="../assets/logo.svg" alt="Element logo" ><div style="font-size: 15px;font-weight: bold;">星宿海</div></img>
    </el-menu-item>
    <!-- <el-menu-item index="/">首页</el-menu-item> -->
    <el-menu-item index="/math">数学</el-menu-item>
    <el-menu-item index="/physics" disabled>物理</el-menu-item>
    <el-menu-item index="/chemistry">化学</el-menu-item>
        <!-- 其他菜单项 -->
    <el-menu-item index="/user/login"> <!-- 配置index为登录页路径 -->
      <div v-if="userInfo">
        <p>当前登录用户：{{ userInfo.username }}</p>
        
        
      </div>
      <div v-else>
            <p>未登录，请登录</p>
          </div>
      
    </el-menu-item>
    <el-menu-item v-if="userInfo"><el-button type="primary" @click="logout">退出登录</el-button></el-menu-item>

    
  </el-menu>
</template>
<style>
.el-menu .el-menu-item {
  font-size: 15px; /* 覆盖菜单项字体 */
}
.el-menu .el-sub-menu__title {
  font-size: 15px; /* 更简洁的选择器，确保应用到所有子菜单标题 */
}
.el-header {
  width: 90%;
  height: 40px;
  padding: 0;
}
.el-menu--horizontal {
  --el-menu-horizontal-height: 50px;
}
.el-menu--horizontal > .el-menu-item:nth-child(1) {
  margin-right: auto;
}
</style>
