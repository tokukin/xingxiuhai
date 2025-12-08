<template>
  <el-page-header icon="" title="当前路径：">
    <template #content>
      <el-breadcrumb separator="/">
        <el-breadcrumb-item
          v-for="(item, index) in breadcrumbList"
          :key="item.path || index"
          :to="item.path"
        >
          {{ item.meta.breadcrumb }}
        </el-breadcrumb-item>
      </el-breadcrumb>
    </template>
  </el-page-header>
</template>

<script setup>
import { useRoute, useRouter } from "vue-router";
import { onMounted, computed, ref } from "vue";

const route = useRoute();
const router = useRouter();
const isRouteReady = ref(false);

// 动态生成面包屑列表（兼容单层/多层父级）
const breadcrumbList = computed(() => {
  if (!isRouteReady.value) return [];

  // 1. 基础匹配的路由（当前路由自身）
  const currentItem = route.matched.find((item) => item.path === route.path);
  if (!currentItem || !currentItem.meta?.breadcrumb) return [];

  // 2. 处理父级：支持数组（多层）或对象（单层）
  const parents = [];
  if (Array.isArray(route.meta?.parentBreadcrumb)) {
    // 多层父级（如 /chemistry/elements 的 [首页, 化学]）
    parents.push(...route.meta.parentBreadcrumb);
  } else if (route.meta?.parentBreadcrumb) {
    // 单层父级（如 /math 的 { 首页 }）
    parents.push(route.meta.parentBreadcrumb);
  }

  // 3. 构建完整面包屑链：[所有父级] + [当前路由]
  const fullList = parents.map((parent) => ({
    path: parent.path,
    meta: { breadcrumb: parent.name },
  }));

  // 4. 添加当前路由（最后一项）
  fullList.push({
    path: currentItem.path,
    meta: { breadcrumb: currentItem.meta.breadcrumb },
  });

  // 5. 去重（避免父级中重复包含首页等）
  return fullList.filter((item, index, self) => {
    return self.findIndex((i) => i.path === item.path) === index;
  });
});

// 当前页面标题（面包屑最后一项）
const currentPageBreadcrumb = computed(() => {
  const list = breadcrumbList.value;
  return list.length > 0 ? list[list.length - 1].meta.breadcrumb : "首页";
});

onMounted(async () => {
  await router.isReady();
  isRouteReady.value = true;
});
</script>
