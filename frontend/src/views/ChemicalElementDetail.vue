<script setup lang="ts">
import { ref, onMounted, onUnmounted } from "vue";
import { useRoute } from "vue-router";
import { ElSelect, ElOption } from "element-plus";

import { useChemicalElementStore } from "@/store/chemicalElementsStore";
import type { ChemicalElementInfo } from "@/types/chemicalelement";
import { log } from "node:console";
import type { TabsPaneContext } from "element-plus";

const chemicalElementStore = useChemicalElementStore();
const elementData = ref<ChemicalElementInfo | null>(null); // 关键：添加这行
// 组件挂载时获取用户信息
/*
onMounted(async () => {
  try {
    const userData: UserInfo = await userStore.fetchUserInfo(2);
    console.log('用户数据:', userData);
  } catch (err) {
    console.error('获取失败:', err);
  }
});*/
const route = useRoute();

// 响应式变量存储窗口大小
const windowSize = ref({
  width: 0,
  height: 0,
  // 可选：添加不含滚动条的尺寸
  clientWidth: 0,
  clientHeight: 0,
});

// 更新窗口大小的函数
const updateWindowSize = () => {
  windowSize.value.width = window.innerWidth;
  windowSize.value.height = window.innerHeight;
  windowSize.value.clientWidth = document.documentElement.clientWidth;
  windowSize.value.clientHeight = document.documentElement.clientHeight;
};
// 批量设置所有 .ratio-item 的高度 = 宽度 × 1.2
const setAllRatioItems = () => {
  updateWindowSize();

  // 获取所有带 .ratio-item 类的元素
  const elementDetail = document.getElementById("element-detail-large");
  if (elementDetail) {
    const width = elementDetail.offsetWidth; // 获取元素宽度
    elementDetail.style.height = `${width * 1.2}px`; // 高度 = 宽度 × 1.2
  }
};

onMounted(async () => {
  try {
    const elementId = Number(route.params.elementId);
    elementData.value = await chemicalElementStore.fetchChemicalElementInfo(
      elementId
    );
    if (elementData.value) {
      console.log("元素数据:", elementData.value);
    } else {
      console.log("元素数据为空");
    }
    const elementDetail = document.getElementById("element-detail-large");
    if (elementDetail) {
      const newDivHtml = `<div class="element-detail-info-header">
      <div class="element-detail-number">${elementData.value.number}</div>
      <div class="element-detail-symbol">${elementData.value.symbol}</div>
      </div>
      <div class="element-detail-info-body">
      <div class="element-detail-chineseName">${elementData.value.chineseName}</div>
      <div class="element-detail-englishName">${elementData.value.englishName}</div>
      <div class="element-detail-electronConfig">${elementData.value.electronConfig}</div>
      <div class="element-detail-type">${elementData.value.type}</div>
 
      </div>
      <div class="element-detail-info-foot">
      
      <div class="element-detail-weight">${elementData.value.weight}</div>
      
      
      </div>`;
      elementDetail.innerHTML += newDivHtml;
      elementDetail.classList.add(elementData.value.type);
    }
  } catch (err) {
    console.error("获取失败:", err);
  }
});

onMounted(() => {
  setAllRatioItems();
  window.addEventListener("resize", setAllRatioItems);
});
onUnmounted(() => {
  window.removeEventListener("resize", setAllRatioItems);
});

// 点击事件处理（明确参数类型）

const handleGetElement = async (elementId: number) => {
  try {
    await chemicalElementStore.fetchChemicalElementInfo(elementId);
  } catch (err) {
    // 处理错误
  }
};

const title = "chemical element";

// 在组件挂载时调用 fetchData 函数
//onMounted(fetchData);

const activeName = ref("first");

const handleClick = (tab: TabsPaneContext, event: Event) => {
  console.log(tab, event);
};
</script>

<template>
  <el-row :gutter="10">
    <el-col :xs="8" :sm="8" :md="8" :lg="8" :xl="8" :offset="8">
      <h1>元素详情</h1>
    </el-col>
  </el-row>
  <hr />

  <el-row :gutter="10">
    <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24">
      <el-tabs v-model="activeName" class="demo-tabs" @tab-click="handleClick">
        <el-tab-pane label="基本情况" name="first">
          <el-row :gutter="10">
            <el-col :xs="2" :sm="2" :md="2" :lg="2" :xl="2" :offset="1">
              <div class="element-detail-text">基<br />本<br />情<br />况</div>
            </el-col>
            <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
              <div class="element-detail-large" id="element-detail-large"></div>
            </el-col>
            <el-col :xs="8" :sm="8" :md="8" :lg="8" :xl="8">
              <div class="element-detail-text">
                <!-- 加 v-if 判断，避免 elementData 为 null 时报错 -->
                <div v-if="elementData">序号：{{ elementData.number }}</div>
                <div v-if="elementData">符号：{{ elementData.symbol }}</div>
                <div v-if="elementData">
                  名称：{{ elementData.chineseName }}
                </div>
                <div v-if="elementData">
                  英文名称：{{ elementData.englishName }}
                </div>

                <div v-else>加载中...</div>
                <!-- 加载状态提示 -->
              </div>
            </el-col>
            <el-col :xs="8" :sm="8" :md="8" :lg="8" :xl="8">
              <div class="element-detail-text">
                <!-- 加 v-if 判断，避免 elementData 为 null 时报错 -->

                <div v-if="elementData">质量：{{ elementData.weight }}</div>

                <div v-if="elementData?.type === 'nonmetal'">
                  类型：{{ elementData.type }}(非金属)
                </div>
                <div v-if="elementData?.type === 'noblegas'">
                  类型：{{ elementData.type }}(稀有气体)
                </div>
                <div v-if="elementData?.type === 'metal'">
                  类型：{{ elementData.type }}(金属)
                </div>
                <div v-if="elementData?.type === 'metalloid'">
                  类型：{{ elementData.type }}(类金属)
                </div>
                <div v-if="elementData?.type === 'halogen'">
                  类型：{{ elementData.type }}(卤素)
                </div>
                <div v-if="elementData?.type === 'actinide'">
                  类型：{{ elementData.type }}(锕系元素)
                </div>
                <div v-if="elementData?.type === 'lanthanide'">
                  类型：{{ elementData.type }}(镧系元素)
                </div>
                <div v-if="elementData?.type === 'transitionmetal'">
                  类型：{{ elementData.type }}(过渡金属)
                </div>
                <div v-if="elementData?.type === 'alkalimetal'">
                  类型：{{ elementData.type }}(碱金属)
                </div>
                <div v-if="elementData?.type === 'alkalineearth'">
                  类型：{{ elementData.type }}(碱土元素)
                </div>
                <div v-if="elementData">
                  第{{ elementData.group }}组；第{{ elementData.period }}周期
                </div>

                <div v-if="elementData">
                  电子排布：{{ elementData.electronConfig }}
                </div>
                <div v-else>加载中...</div>
                <!-- 加载状态提示 -->
              </div>
            </el-col>
          </el-row>
        </el-tab-pane>
        <el-tab-pane label="选项一" name="second">选项一</el-tab-pane>
        <el-tab-pane label="选项二" name="third">选项二</el-tab-pane>
        <el-tab-pane label="选项三" name="fourth">选项三</el-tab-pane>
      </el-tabs>
    </el-col>
  </el-row>
</template>
<style scoped>
#element-detail-large {
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  color: aliceblue;
}
:deep(.element-detail-info-header) {
  display: flex;
  flex-direction: row;
  justify-content: center; /* 垂直方向居中（主轴居中） */
  align-items: center; /* 水平方向居中（交叉轴居中） */
  width: 100%; /* 确保容器宽度 */
  height: 20%;
  /* padding-top: 5%; */
}
:deep(.element-detail-info-body) {
  display: flex;
  flex-direction: column;
  justify-content: center; /* 垂直方向居中（主轴居中） */
  align-items: center; /* 水平方向居中（交叉轴居中） */
  width: 100%; /* 确保容器宽度 */

  height: 60%;
}
:deep(.element-detail-info-foot) {
  display: flex;
  flex-direction: row;
  justify-content: center; /* 垂直方向居中（主轴居中） */
  align-items: center; /* 水平方向居中（交叉轴居中） */
  width: 100%; /* 确保容器宽度 */
  height: 20%;
  /* padding-top: 5%; */
}
:deep(.element-detail-info-header .element-detail-number) {
  font-size: 24px;
  font-weight: bold;
  width: 50%;
  text-align: left;
  padding-left: 5%;
  font-size: clamp(5px, 3vw, 50px);
}
:deep(.element-detail-info-header .element-detail-symbol) {
  font-size: 24px;
  font-weight: bold;
  width: 50%;
  text-align: right;
  padding-right: 5%;
  font-size: clamp(5px, 3vw, 50px);
}
:deep(.element-detail-info-body .element-detail-chineseName) {
  font-weight: bold;
  text-align: center;
  font-size: clamp(20px, 3vw, 200px);
}
:deep(.element-detail-info-body .element-detail-englishName) {
  font-weight: bold;
  text-align: center;
  font-size: clamp(10px, 3vw, 50px);
}
:deep(.element-detail-info-body .element-detail-electronConfig) {
  font-weight: bold;
  text-align: center;
  font-size: clamp(8px, 3vw, 45px);
}
:deep(.element-detail-info-body .element-detail-type) {
  font-weight: bold;
  text-align: center;
  font-size: clamp(8px, 3vw, 40px);
}
:deep(.element-detail-info-body .element-detail-group) {
  font-weight: bold;
  text-align: center;
  font-size: clamp(8px, 3vw, 35px);
}
:deep(.element-detail-info-body .element-detail-period) {
  font-weight: bold;
  text-align: center;
  font-size: clamp(8px, 3vw, 35px);
}
:deep(.element-detail-info-foot .element-detail-weight) {
  font-weight: bold;
  text-align: center;
  font-size: clamp(5px, 3vw, 45px);
}
:deep(.element-detail-text) {
  display: flex;
  flex-direction: column;
  justify-content: center; /* 垂直方向居中（主轴居中） */
  align-items: center; /* 水平方向居中（交叉轴居中） */
  font-size: clamp(20px, 3vw, 30px);
  line-height: 1.5;
  margin-bottom: 10px;
  font-weight: bold;
  background-color: #3966a2;
  color: aliceblue;
  height: 100%;
}
</style>
