import { createWebHashHistory, createRouter } from "vue-router";

const routes = [
  {
    path: "/", // 路由路径
    // name: "Home", // 路由名称（可选）
    component: () => import("../views/Home.vue"),
    meta: { title: "首页", breadcrumb: "首页" },
  },
  {
    path: "/user/login", // 路由路径
    name: "Login",
    // name: "Home", // 路由名称（可选）
    component: () => import("../views/Login.vue"),

    meta: {
      title: "登录",
      breadcrumb: "登录",
      parentBreadcrumb: { path: "/", name: "首页" }, // 新增
    },
  },
  {
    path: "/math",
    name: "Math",
    component: () => import("../views/MathHome.vue"),
    meta: {
      title: "数学",
      breadcrumb: "数学",
      parentBreadcrumb: { path: "/", name: "首页" },
      requiresAuth: true, // 标记：需要登录才能访问
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
        { path: "/math", name: "数学" }, // 第二层父级
      ],
      requiresAuth: true, // 标记：需要登录才能访问
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
      requiresAuth: true, // 标记：需要登录才能访问
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
      requiresAuth: true, // 标记：需要登录才能访问
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
      requiresAuth: true, // 标记：需要登录才能访问
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
      requiresAuth: true, // 标记：需要登录才能访问
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

// 路由守卫：验证登录状态
router.beforeEach((to, from, next) => {
  // 1. 获取登录状态（从 localStorage 读取 token，和后端保持一致）
  const isLogin = !!localStorage.getItem("access_token");

  // 2. 检查目标路由是否需要鉴权
  const needAuth = to.meta.requiresAuth;

  if (needAuth) {
    // 3. 需要鉴权：已登录则放行，未登录则跳登录页（记录来源路径）
    if (isLogin) {
      next(); // 已登录，正常跳转
    } else {
      // 跳登录页，并携带「想要访问的路径」（登录后可返回）
      next({
        path: "/user/login",
        query: { redirect: to.fullPath }, // 记录原路径，如 /math
      });
    }
  } else {
    // 4. 无需鉴权：直接放行（如登录页、首页）
    next();
  }
});
export default router;
