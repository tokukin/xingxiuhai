<script setup>
import PageHeader from "@/components/PageHeader.vue";
import MeunRight from "@/components/MeunRight.vue";
import { useRoute, useRouter } from "vue-router";
import bus from "@/utils/bus"; // 导入事件总线
import { ref, onMounted, onUnmounted } from "vue";

const router = useRouter();
const route = useRoute();
console.log(route.path);
</script>

<template>
  <MeunRight />
  <PageHeader />

  <el-container>
    <el-main>
      <router-view />
    </el-main>
  </el-container>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
