import { createWebHashHistory, createRouter } from "vue-router";

const routes = [
  {
    path: "/", // 路由路径
    // name: "Home", // 路由名称（可选）
    component: () => import("../views/Home.vue"),
    meta: { title: "首页", breadcrumb: "首页" },
  },
  {
    path: "/math",
    name: "Math",
    component: () => import("../views/MathHome.vue"),
    meta: {
      title: "数学",
      breadcrumb: "数学",
      parentBreadcrumb: { path: "/", name: "首页" },
    },
  },
  // /math/calculator
  {
    path: "/math/calculator",
    name: "Calculator",
    component: () => import("../views/MathCalculator.vue"),
    meta: {
      title: "计算器",
      breadcrumb: "计算器",
      parentBreadcrumb: [
        { path: "/", name: "首页" }, // 第一层父级
        { path: "/math", name: "数学" },
      ],
    },
  },
  // /physics
  {
    path: "/physics",
    name: "Physics",
    component: () => import("../views/Physics.vue"),
    meta: {
      title: "物理",
      breadcrumb: "物理",
      parentBreadcrumb: { path: "/", name: "首页" },
    },
  },
  {
    path: "/chemistry",
    name: "Chemistry",
    component: () => import("../views/Chemistry.vue"),
    meta: {
      title: "化学",
      breadcrumb: "化学",
      parentBreadcrumb: { path: "/", name: "首页" },
    },
    children: [],
  },
  {
    path: "/chemistry/periodic-table",
    name: "periodic-table",
    component: () => import("../views/ChemicalElements.vue"),
    meta: {
      title: "元素周期表",
      breadcrumb: "元素周期表",
      parentBreadcrumb: [
        { path: "/", name: "首页" }, // 第一层父级
        { path: "/chemistry", name: "化学" },
      ],
    },
  },
  ///chemistry/other
  {
    path: "/chemistry/other",
    name: "ChemicalElements",
    component: () => import("../views/che_test.vue"),
    meta: {
      title: "元素周期表",
      breadcrumb: "元素周期表_test",
      parentBreadcrumb: [
        { path: "/", name: "首页" }, // 第一层父级
        { path: "/chemistry", name: "化学" },
      ],
    },
  },

  {
    // 404 路由（放在最后）
    path: "/:pathMatch(.*)*", // 匹配所有未定义的路由
    name: "NotFound",
    component: () => import("../views/NotFound.vue"), // 懒加载 404 页面
    meta: {
      title: "404 未找到",
      breadcrumb: "404 未找到",
      parentBreadcrumb: { path: "/", name: "首页" },
    },
  },
];

// 创建路由实例
const router = createRouter({
  history: createWebHashHistory(),
  routes,
});
export default router;
