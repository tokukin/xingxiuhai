import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import router from "./router";
import naive from "naive-ui";

import ElementPlus from "element-plus";
import "element-plus/dist/index.css";

createApp(App).use(router).use(naive).use(ElementPlus).mount("#app");
