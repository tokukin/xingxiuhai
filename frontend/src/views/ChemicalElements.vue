<script setup>
import { c } from "naive-ui";
import { ref, onMounted, onUnmounted } from "vue";

const title = "元素周期表";
const gutterSize = ref(2);
var allElements = [];
const loadAllElements = () => {
  fetch("/api/v1/chemical/element/all")
    .then((response) => response.json())
    .then((data) => {
      console.log("全量元素加载完成");
      // console.log(data);
      allElements = data.data;
      const elementSamples = Array.from(
        document.querySelectorAll(".element-type-sample")
      );
      elementSamples.forEach((elementSample) => {
        elementSample.classList.remove("element-type-sample-large");
        elementSample.classList.remove("element-type-sample-mid");
        elementSample.classList.remove("element-type-sample-small");
      });
      const elementDomo = document.getElementById("grid-element-demo-detail");
      if (elementDomo) {
        let elem = allElements[0];
        elementDomo.textContent = "";
        const newDivHtml = `<div class="element-detail-info-header">
      <div class="element-detail-number">${elem.atomic}</div>
      <div class="element-detail-symbol">${elem.symbol}</div>
      </div>
      <div class="element-detail-info-body">
      <div class="element-detail-chineseName">${elem.chinesename}</div>
      <div class="element-detail-englishName">${elem.englishname}</div>
      <div class="element-detail-electronConfig">${elem.electronstring}</div>
      <div class="element-detail-type">${elem.series}</div>
 
      </div>
      <div class="element-detail-info-foot">
      
      <div class="element-detail-weight">${elem.weight}</div>
      
      
      </div>`;
        elementDomo.innerHTML += newDivHtml;

        elementDomo.classList.add(elem.type);
      }
      if (windowSize.value.clientWidth > 1970) {
        elementSamples.forEach((elementSample) => {
          elementSample.classList.add("element-type-sample-large");
        });
        for (let elem of allElements) {
          //console.log(elem.type);

          var elementDom = document.getElementById(`element-${elem.atomic}`);
          if (elementDom) {
            // 修改元素名称（找到 .element-name 类的子元素）
            // const newDivHtml = `${elem.symbol}`;
            const newDivHtml = `<div class="element-info-up"><div class="element-number">${elem.atomic}</div><div class="element-symbol">${elem.symbol}</div></div><div class="element-info-mid"><div class="element-chineseName">${elem.chinesename}</div></div>`;
            elementDom.innerHTML += newDivHtml;
            elementDom.classList.add(elem.series);
          }
        }
        var elementDoms = Array.from(
          document.querySelectorAll(".lanthanide-sample")
        );
        elementDoms.forEach((elementDom) => {
          const newDivHtml = `57-71<br />镧系`;
          elementDom.innerHTML += newDivHtml;
          elementDom.classList.add("nide-sample");
        });
        var elementDoms = Array.from(
          document.querySelectorAll(".actinide-sample")
        );
        elementDoms.forEach((elementDom) => {
          const newDivHtml = `89-103<br />锕系`;
          elementDom.innerHTML += newDivHtml;
          elementDom.classList.add("nide-sample");
        });
      } else if (windowSize.value.clientWidth > 1300) {
        elementSamples.forEach((elementSample) => {
          elementSample.classList.add("element-type-sample-mid");
        });
        for (let elem of allElements) {
          //console.log(elem.type);

          var elementDom = document.getElementById(`element-${elem.atomic}`);
          if (elementDom) {
            // 修改元素名称（找到 .element-name 类的子元素）
            // const newDivHtml = `${elem.symbol}`;
            const newDivHtml = `<div class="element-info-up"><div class="element-number-mid">${elem.atomic}</div></div><div class="element-info-mid"><div class="element-symbol-mid">${elem.symbol}</div></div>`;
            elementDom.innerHTML += newDivHtml;
            elementDom.classList.add(elem.series);
          }
        }
        var elementDoms = Array.from(
          document.querySelectorAll(".lanthanide-sample")
        );
        elementDoms.forEach((elementDom) => {
          const newDivHtml = `57-71<br />镧系`;
          elementDom.innerHTML += newDivHtml;
          elementDom.classList.add("nide-sample-mid");
        });
        var elementDoms = Array.from(
          document.querySelectorAll(".actinide-sample")
        );
        elementDoms.forEach((elementDom) => {
          const newDivHtml = `89-103<br />锕系`;
          elementDom.innerHTML += newDivHtml;
          elementDom.classList.add("nide-sample-mid");
        });
      } else {
        elementSamples.forEach((elementSample) => {
          elementSample.classList.add("element-type-sample-small");
        });
        for (let elem of allElements) {
          //console.log(elem.type);

          var elementDom = document.getElementById(`element-${elem.atomic}`);
          if (elementDom) {
            // 修改元素名称（找到 .element-name 类的子元素）
            // const newDivHtml = `${elem.symbol}`;
            const newDivHtml = `<div class="element-symbol-small">${elem.symbol}</div>`;
            elementDom.innerHTML += newDivHtml;
            elementDom.classList.add(elem.series);
          }
        }
        var elementDoms = Array.from(
          document.querySelectorAll(".lanthanide-sample")
        );
        elementDoms.forEach((elementDom) => {
          const newDivHtml = `57-71<br />镧系`;
          elementDom.innerHTML += newDivHtml;
          elementDom.classList.add("nide-sample-small");
        });
        var elementDoms = Array.from(
          document.querySelectorAll(".actinide-sample")
        );
        elementDoms.forEach((elementDom) => {
          const newDivHtml = `89-103<br />锕系`;
          elementDom.innerHTML += newDivHtml;
          elementDom.classList.add("nide-sample-small");
        });
      }
    })
    .catch((error) => {
      console.error("Error:", error);
    });
};
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

  const items = Array.from(document.querySelectorAll(".grid-element"));

  items.forEach((item) => {
    if (item) {
      const width = item.offsetWidth;
      item.style.height = `${width * 1.2}px`;
    }
  });

  clearGridElements();
  loadAllElements();
};

const clearGridElements = () => {
  // 获取所有 .grid-element 元素
  const gridElements = Array.from(document.querySelectorAll(".grid-element"));

  gridElements.forEach((el) => {
    if (el.id) {
      // 1. 清除所有子内容（包括文本和嵌套元素）
      el.innerHTML = "";

      // 2. 仅保留 grid-element 类，移除其他所有类
      // 先获取当前所有类名
      const classes = el.classList;
      // 过滤出需要保留的类（仅 grid-element）
      const classesToKeep = Array.from(classes).filter(
        (cls) => cls === "grid-element"
      );
      // 移除所有类，再重新添加需要保留的类
      el.className = classesToKeep.join(" ");
    }
  });
};

// 初始化时设置
onMounted(() => {
  console.log("template 加载完成！DOM 已就绪");
  setAllRatioItems();

  window.addEventListener("resize", setAllRatioItems);
  const gridElements = document.querySelectorAll(".grid-element");

  gridElements.forEach((el) => {
    el.addEventListener("mouseenter", () => {
      const elementId = el.id.split("-").slice(-1)[0];
      if (elementId) {
        // console.log(elementId);
        const elementDomo = document.getElementById("grid-element-demo-detail");
        if (elementDomo) {
          for (let elem of allElements) {
            if (elem.atomic.toString() == `${elementId}`) {
              console.log(elem);
              elementDomo.textContent = "";

              const newDivHtml = `<div class="element-detail-info-header">
      <div class="element-detail-number">${elem.atomic}</div>
      <div class="element-detail-symbol">${elem.symbol}</div>
      </div>
      <div class="element-detail-info-body">
      <div class="element-detail-chineseName">${elem.chinesename}</div>
      <div class="element-detail-englishName">${elem.englishname}</div>
      <div class="element-detail-electronConfig">${elem.electronstring}</div>
      <div class="element-detail-type">${elem.series}</div>
 
      </div>
      <div class="element-detail-info-foot">
      
      <div class="element-detail-weight">${elem.weight}</div>
      
      
      </div>`;
              elementDomo.innerHTML += newDivHtml;

              elementDomo.classList.add(elem.series);
            }
          }
        }
      }
    });

    el.addEventListener("mouseleave", () => {
      const elementDomo = document.getElementById("grid-element-demo-detail");

      if (elementDomo) {
        elementDomo.classList.remove(...elementDomo.classList);
        const elementId = 1;
        if (elementId) {
          const elementDomo = document.getElementById(
            "grid-element-demo-detail"
          );
          if (elementDomo) {
            for (let elem of allElements) {
              if (elem.atomic.toString() == `${elementId}`) {
                console.log(elem);
                elementDomo.textContent = "";

                const newDivHtml = `<div class="element-detail-info-header">
      <div class="element-detail-number">${elem.atomic}</div>
      <div class="element-detail-symbol">${elem.symbol}</div>
      </div>
      <div class="element-detail-info-body">
      <div class="element-detail-chineseName">${elem.chinesename}</div>
      <div class="element-detail-englishName">${elem.englishname}</div>
      <div class="element-detail-electronConfig">${elem.electronstring}</div>
      <div class="element-detail-type">${elem.series}</div>
 
      </div>
      <div class="element-detail-info-foot">
      
      <div class="element-detail-weight">${elem.weight}</div>
      
      
      </div>`;
                elementDomo.innerHTML += newDivHtml;

                elementDomo.classList.add(elem.series);
              }
            }
          }
        }
      }

      if (elementDomo) {
      }
    });
  });
});

// 组件卸载时清理事件监听
onUnmounted(() => {
  window.removeEventListener("resize", setAllRatioItems);
});
</script>

<template>
  <h1 style="text-align: center; font-size: 30px; margin: 5px">{{ title }}</h1>

  <el-row :gutter="gutterSize" class="period-row">
    <el-col :xs="18" :sm="18" :md="18" :lg="18" :xl="18" :offset="3">
      <el-row :gutter="gutterSize">
        <el-col :xs="2" :sm="2" :md="2" :lg="2" :xl="2" :offset="2">
          <div class="element-type-sample nonmetal">nonmetal<br />非金属</div>
        </el-col>
        <el-col :xs="2" :sm="2" :md="2" :lg="2" :xl="2">
          <div class="element-type-sample noblegas">
            noblegas<br />
            稀有气体
          </div>
        </el-col>
        <el-col :xs="2" :sm="2" :md="2" :lg="2" :xl="2">
          <div class="element-type-sample alkalimetal">
            alkalimetal<br />碱金属
          </div>
        </el-col>
        <el-col :xs="2" :sm="2" :md="2" :lg="2" :xl="2">
          <div class="element-type-sample alkalineearth">
            alkalineearth<br />碱土金属
          </div>
        </el-col>
        <el-col :xs="2" :sm="2" :md="2" :lg="2" :xl="2">
          <div class="element-type-sample metalloid">metalloid<br />类金属</div>
        </el-col>
        <el-col :xs="2" :sm="2" :md="2" :lg="2" :xl="2">
          <div class="element-type-sample transitionmetal">
            transitionmetal<br />过渡金属
          </div>
        </el-col>
        <el-col :xs="2" :sm="2" :md="2" :lg="2" :xl="2">
          <div class="element-type-sample halogen">halogen<br />卤素</div>
        </el-col>
        <el-col :xs="2" :sm="2" :md="2" :lg="2" :xl="2">
          <div class="element-type-sample metal">metal<br />金属</div>
        </el-col>
        <el-col :xs="2" :sm="2" :md="2" :lg="2" :xl="2">
          <div class="element-type-sample lanthanide">
            lanthanide<br />镧系元素
          </div>
        </el-col>
        <el-col :xs="2" :sm="2" :md="2" :lg="2" :xl="2">
          <div class="element-type-sample actinide">actinide<br />锕系元素</div>
        </el-col>
      </el-row>
    </el-col>
  </el-row>
  <div class="element-gap"></div>
  <el-row :gutter="gutterSize" class="period-row">
    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6" :offset="3">
      <el-row :gutter="gutterSize">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-1"></div>
        </el-col>
        <el-col :xs="8" :sm="8" :md="8" :lg="8" :xl="8" :offset="8">
          <div id="grid-element-demo">
            <div class="element-detail-info-header">
              <div class="element-detail-number">序号</div>
              <div class="element-detail-symbol">符号</div>
            </div>
            <div class="element-detail-info-body">
              <div class="element-detail-chineseName">中文名</div>
              <div class="element-detail-englishName">英文名</div>
              <div class="element-detail-electronConfig">电子排布</div>
              <div class="element-detail-type">类型</div>
            </div>
            <div class="element-detail-info-foot">
              <div class="element-detail-weight">原子量</div>
            </div>
          </div>
        </el-col>
      </el-row>
    </el-col>
    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6">
      <el-row :gutter="gutterSize">
        <el-col :xs="8" :sm="8" :md="8" :lg="8" :xl="8">
          <div id="grid-element-demo-detail"></div>
        </el-col>
      </el-row>
    </el-col>

    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6" :offset="1">
      <el-row :gutter="gutterSize">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4" :offset="16">
          <div class="grid-element" id="element-2"></div>
        </el-col>
      </el-row>
    </el-col>
  </el-row>
  <el-row :gutter="gutterSize" class="period-row">
    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6" :offset="3">
      <el-row :gutter="gutterSize">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-3"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-4"></div>
        </el-col>
      </el-row>
    </el-col>

    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6" :offset="6">
      <el-row :gutter="gutterSize">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-5"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-6"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-7"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-8"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-9"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-10"></div>
        </el-col>
      </el-row>
    </el-col>
  </el-row>
  <el-row :gutter="gutterSize" class="period-row">
    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6" :offset="3">
      <el-row :gutter="gutterSize">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-11"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-12"></div>
        </el-col>
      </el-row>
    </el-col>

    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6" :offset="6">
      <el-row :gutter="gutterSize">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-13"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-14"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-15"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-16"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-17"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-18"></div>
        </el-col>
      </el-row>
    </el-col>
  </el-row>
  <el-row :gutter="gutterSize" class="period-row">
    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6" :offset="3">
      <el-row :gutter="gutterSize">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-19"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-20"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-21"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-22"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-23"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-24"></div>
        </el-col>
      </el-row>
    </el-col>
    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6">
      <el-row :gutter="gutterSize">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-25"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-26"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-27"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-28"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-29"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-30"></div>
        </el-col>
      </el-row>
    </el-col>

    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6">
      <el-row :gutter="gutterSize">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-31"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-32"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-33"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-34"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-35"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-36"></div>
        </el-col>
      </el-row>
    </el-col>
  </el-row>
  <el-row :gutter="gutterSize" class="period-row">
    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6" :offset="3">
      <el-row :gutter="gutterSize">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-37"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-38"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-39"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-40"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-41"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-42"></div>
        </el-col>
      </el-row>
    </el-col>
    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6">
      <el-row :gutter="gutterSize">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-43"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-44"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-45"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-46"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-47"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-48"></div>
        </el-col>
      </el-row>
    </el-col>

    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6">
      <el-row :gutter="gutterSize">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-49"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-50"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-51"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-52"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-53"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-54"></div>
        </el-col>
      </el-row>
    </el-col>
  </el-row>
  <el-row :gutter="gutterSize" class="period-row">
    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6" :offset="3">
      <el-row :gutter="gutterSize">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-55"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-56"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element lanthanide-sample"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-72"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-73"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-74"></div>
        </el-col>
      </el-row>
    </el-col>
    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6">
      <el-row :gutter="gutterSize">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-75"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-76"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-77"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-78"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-79"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-80"></div>
        </el-col>
      </el-row>
    </el-col>

    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6">
      <el-row :gutter="gutterSize">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-81"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-82"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-83"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-84"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-85"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-86"></div>
        </el-col>
      </el-row>
    </el-col>
  </el-row>
  <el-row :gutter="gutterSize" class="period-row">
    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6" :offset="3">
      <el-row :gutter="gutterSize">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-87"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-88"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element actinide-sample"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-104"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-105"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-106"></div>
        </el-col>
      </el-row>
    </el-col>
    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6">
      <el-row :gutter="gutterSize">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-107"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-108"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-109"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-110"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-111"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-112"></div>
        </el-col>
      </el-row>
    </el-col>

    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6">
      <el-row :gutter="gutterSize">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-113"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-114"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-115"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-116"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-117"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-118"></div>
        </el-col>
      </el-row>
    </el-col>
  </el-row>
  <div class="element-gap"></div>
  <el-row :gutter="gutterSize" class="period-row">
    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6" :offset="3">
      <el-row :gutter="gutterSize">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4" :offset="4">
          <div class="grid-element lanthanide-sample"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-57"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-58"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-59"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-60"></div>
        </el-col>
      </el-row>
    </el-col>
    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6">
      <el-row :gutter="gutterSize">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-61"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-62"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-63"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-64"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-65"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-66"></div>
        </el-col>
      </el-row>
    </el-col>

    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6">
      <el-row :gutter="gutterSize">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-67"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-68"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-69"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-70"></div>
        </el-col>

        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-71"></div>
        </el-col>
      </el-row>
    </el-col>
  </el-row>
  <el-row :gutter="gutterSize" class="period-row">
    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6" :offset="3">
      <el-row :gutter="gutterSize">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4" :offset="4">
          <div class="grid-element actinide-sample"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-89"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-90"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-91"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-92"></div>
        </el-col>
      </el-row>
    </el-col>
    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6">
      <el-row :gutter="gutterSize">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-93"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-94"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-95"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-96"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-97"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-98"></div>
        </el-col>
      </el-row>
    </el-col>

    <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6">
      <el-row :gutter="gutterSize">
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-99"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-100"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-101"></div>
        </el-col>
        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-102"></div>
        </el-col>

        <el-col :xs="4" :sm="4" :md="4" :lg="4" :xl="4">
          <div class="grid-element" id="element-103"></div>
        </el-col>
      </el-row>
    </el-col>
  </el-row>

  <!-- 添加按钮，点击触发 increment 函数 -->
</template>
<style scoped>
/* 给选择框添加一点样式 */

.grid-element {
  border-radius: 4px;
  display: flex;
  flex-direction: column;
  color: aliceblue;
  background-color: blueviolet;
}
#grid-element-demo {
  border-radius: 4px;
  display: flex;
  flex-direction: column;
  color: aliceblue;
  background-color: blueviolet;
  position: absolute;
  z-index: 1000;
  width: 9vw;
  height: 10.8vw;
  margin-top: 1vw;
}
#grid-element-demo-detail {
  border-radius: 4px;
  display: flex;
  flex-direction: column;
  color: aliceblue;
  background-color: blueviolet;
  position: absolute;
  z-index: 1000;
  width: 9vw;
  height: 10.8vw;
  margin-top: 1vw;
}
/* 动态效果 */
.grid-element:active,
.grid-element:focus,
.grid-element:hover {
  transform: scale(1.05); /* 点击/悬浮时轻微放大 */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* 添加阴影增强立体感 */
  cursor: pointer;
}

/* .element-info-up 内部：水平行排列 */
:deep(.element-info-up) {
  display: flex;
  flex-direction: row;
  width: 100%; /* 确保容器宽度 */
  height: 30px;
  padding-top: 2%;
}
:deep(.element-info-up .element-number) {
  display: inline-block;
  width: 40%;
  text-align: left;
  overflow: hidden;
  text-overflow: ellipsis; /* 防止内容过长 */
  padding-left: 2%;

  text-align: center;
}
:deep(.element-info-up .element-number-mid) {
  display: inline-block;
  width: 100%;
  overflow: hidden;
  text-overflow: ellipsis; /* 防止内容过长 */
  padding-left: 2%;

  text-align: center;
}
:deep(.element-info-up .element-symbol) {
  display: inline-block;
  width: 45%;
  text-align: right;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  padding-right: 2%;
}
:deep(.element-symbol-small) {
  justify-content: center;
  text-align: center;
  height: 100%;
  width: 100%;
}
:deep(.element-info-mid .element-symbol-mid) {
  display: inline-block;
  width: 100%;
  text-align: center;
  font-size: clamp(12px, 3vw, 20px);
}
:deep(.element-info-mid) {
  height: 50px;
  display: flex;
  flex-direction: column; /* 垂直排列子元素 */
  justify-content: center; /* 垂直方向居中（主轴居中） */
  align-items: center; /* 水平方向居中（交叉轴居中） */
}
:deep(.element-info-mid .element-chineseName) {
  font-size: clamp(12px, 3vw, 23px);
}

.period-row {
  margin-bottom: 2px;
}

.element-type-sample {
  border-radius: 4px;
  display: flex;
  flex-direction: column;
  color: aliceblue;
  font-size: clamp(6px, 3vw, 16px);
  justify-content: center;
  align-items: center;
  text-overflow: ellipsis;
  height: 50px;
}
:deep(.element-type-sample-large) {
  font-size: clamp(6px, 3vw, 16px);
  justify-content: center;
  align-items: center;
  text-overflow: ellipsis;
}
:deep(.element-type-sample-mid) {
  font-size: clamp(6px, 3vw, 10px);
  justify-content: center;
  align-items: center;
  text-overflow: ellipsis;
}
:deep(.element-type-sample-small) {
  font-size: clamp(6px, 3vw, 8px);
  justify-content: center;
  align-items: center;
  text-overflow: ellipsis;
}

:deep(.nide-sample) {
  font-size: clamp(6px, 3vw, 16px);
  justify-content: center;
  align-items: center;
}
:deep(.nide-sample-mid) {
  font-size: clamp(6px, 3vw, 10px);
  justify-content: center;
  align-items: center;
}
:deep(.nide-sample-small) {
  font-size: clamp(6px, 3vw, 8px);
  justify-content: center;
  align-items: center;
}
.element-gap {
  margin-top: 20px;
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
  font-size: 1vw;
}
:deep(.element-detail-info-header .element-detail-symbol) {
  font-size: 24px;
  font-weight: bold;
  width: 50%;
  text-align: right;
  padding-right: 5%;
  font-size: 1vw;
}
:deep(.element-detail-info-body .element-detail-chineseName) {
  font-weight: bold;
  text-align: center;
  font-size: 2vw;
}
:deep(.element-detail-info-body .element-detail-englishName) {
  font-weight: bold;
  text-align: center;
  font-size: 0.8vw;
}
:deep(.element-detail-info-body .element-detail-electronConfig) {
  font-weight: bold;
  text-align: center;
  font-size: 0.7vw;
}
:deep(.element-detail-info-body .element-detail-type) {
  font-weight: bold;
  text-align: center;
  font-size: 0.7vw;
}
:deep(.element-detail-info-body .element-detail-group) {
  font-weight: bold;
  text-align: center;
  font-size: 1vw;
}
:deep(.element-detail-info-body .element-detail-period) {
  font-weight: bold;
  text-align: center;
  font-size: 1vw;
}
:deep(.element-detail-info-foot .element-detail-weight) {
  font-weight: bold;
  text-align: center;
  font-size: 1vw;
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
