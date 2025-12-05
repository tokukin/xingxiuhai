<script setup>
import { ref } from "vue";

const gutterSize = ref(10);
const value = ref([]); // 年级选择器绑定值
const levelValue = ref([]); // 知识点选择器绑定值
// 关键修复：重新定义 isLoading 响应式变量
const isLoading = ref(false);

// 知识点选项（一级结构）
const options_level = ref([]);

const total_answered = ref(0);
const correct_answers = ref(0);
const current_problem_id = ref(1);

const expression = ref("1+1");
const answer = ref(0);

// 年级选择变化处理
const handleChange = (val) => {
  if (val && val.length === 3) {
    load_level(val[2]);
  } else {
    resetOptionsLevel();
  }
};

// 口算等级选择处理
const handleChange_level = (val) => {
  console.log("选中口算等级：", val);
  get_question(val);
};

// 重置口算等级选项
const resetOptionsLevel = () => {
  options_level.value = [];
  levelValue.value = [];
  isLoading.value = false;
};

// 年级选项（规范 value 命名）
const options = [
  {
    value: "primary",
    label: "小学",
    children: [
      {
        value: "grade1",
        label: "一年级",
        children: [
          { value: "1", label: "上册" },
          { value: "2", label: "下册" },
        ],
      },
      {
        value: "grade2",
        label: "二年级",
        children: [
          { value: "3", label: "上册" },
          { value: "4", label: "下册" },
        ],
      },
      {
        value: "grade3",
        label: "三年级",
        children: [
          { value: "5", label: "上册" },
          { value: "6", label: "下册" },
        ],
      },
      {
        value: "grade4",
        label: "四年级",
        children: [
          { value: "7", label: "上册" },
          { value: "8", label: "下册" },
        ],
      },
      {
        value: "grade5",
        label: "五年级",
        children: [
          { value: "9", label: "上册" },
          { value: "10", label: "下册" },
        ],
      },
      {
        value: "grade6",
        label: "六年级",
        children: [
          { value: "11", label: "上册" },
          { value: "12", label: "下册" },
        ],
      },
    ],
  },
  {
    value: "middle",
    label: "初中",
    children: [
      {
        value: "grade7",
        label: "初一",
        children: [
          { value: "13", label: "上册" },
          { value: "14", label: "下册" },
        ],
      },
      {
        value: "grade8",
        label: "初二",
        children: [
          { value: "15", label: "上册" },
          { value: "16", label: "下册" },
        ],
      },
      {
        value: "grade9",
        label: "初三",
        children: [
          { value: "17", label: "上册" },
          { value: "18", label: "下册" },
        ],
      },
    ],
  },
  {
    value: "high",
    label: "高中",
    children: [
      {
        value: "grade10",
        label: "高一",
        children: [
          { value: "19", label: "上册" },
          { value: "20", label: "下册" },
        ],
      },
      {
        value: "grade11",
        label: "高二",
        children: [
          { value: "21", label: "上册" },
          { value: "22", label: "下册" },
        ],
      },
      {
        value: "grade12",
        label: "高三",
        children: [
          { value: "23", label: "上册" },
          { value: "24", label: "下册" },
        ],
      },
    ],
  },
];

// 加载知识点
const load_level = async (grade_id) => {
  if (!grade_id) return;
  isLoading.value = true;
  try {
    resetOptionsLevel();
    const response = await fetch(`/api/v1/math/level?grade_id=${grade_id}`);
    if (!response.ok) throw new Error("接口请求失败");

    const data = await response.json();
    console.log(data);
    if (
      data?.status === 200 &&
      Array.isArray(data.data) &&
      data.data.length > 0
    ) {
      const newLevels = data.data.map((level, index) => ({
        value: `${grade_id}`,
        label: level.calculate_level || "未命名口算等级",
      }));
      options_level.value = options_level.value.concat(newLevels);
    } else {
      console.log("该年级暂无口算等级数据");
    }
  } catch (error) {
    console.error("加载口算等级失败：", error.message);
    resetOptionsLevel();
  } finally {
    isLoading.value = false;
  }
};
//出题
const get_question = (level) => {
  fetch(`api/v1/math/problem?level=${level}`)
    .then((response) => response.json())
    .then((data) => {
      //console.log(data);
      if (data?.status === 200 && data.data) {
        console.log(data.data);
        expression.value = data.data.expression;
        answer.value = data.data.answer;
      }
    })
    .catch((error) => {
      console.error("Error:", error);
    });
};
</script>

<template>
  <h2>数学口算</h2>
  <el-row :gutter="gutterSize" class="select_point_row">
    <!-- 年级选择器 -->
    <el-col :xs="10" :sm="10" :md="10" :lg="10" :xl="10">
      <el-row :gutter="gutterSize" class="select_point">
        <el-col
          class="select_point_text"
          :xs="8"
          :sm="8"
          :md="8"
          :lg="8"
          :xl="8"
        >
          <div>请选择年级及学期</div>
        </el-col>
        <el-col
          class="select_point_select"
          :xs="16"
          :sm="16"
          :md="16"
          :lg="16"
          :xl="16"
        >
          <el-cascader
            v-model="value"
            style="width: 100%"
            size="large"
            placeholder="请选择年级及学期"
            :options="options"
            @change="handleChange"
            :props="{
              expandTrigger: 'hover',
              checkStrictly: true,
              emitPath: true,
            }"
            :disabled="isLoading"
          />
        </el-col>
      </el-row>
    </el-col>

    <!-- 知识点选择器 -->
    <el-col :xs="12" :sm="12" :md="12" :lg="12" :xl="12">
      <el-row :gutter="gutterSize" class="select_point">
        <el-col
          class="select_point_text"
          :xs="8"
          :sm="8"
          :md="8"
          :lg="8"
          :xl="8"
        >
          <div>请选择口算等级</div>
        </el-col>
        <el-col
          class="select_point_select"
          :xs="16"
          :sm="16"
          :md="16"
          :lg="16"
          :xl="16"
        >
          <el-select
            v-model="levelValue"
            style="width: 100%"
            size="large"
            placeholder="请正确选择口算等级"
            @change="handleChange_level"
            :disabled="isLoading"
          >
            <el-option
              v-for="item in options_level"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            />
          </el-select>
        </el-col>
      </el-row>
    </el-col>
  </el-row>
  <el-row class="calc_box">
    <div class="calc_box_info">
      <div>
        题号:<el-tag type="primary" class="ans_info"
          >第{{ current_problem_id }}题</el-tag
        >
      </div>
      <div>
        总答题:<el-tag type="primary" class="ans_info">{{
          total_answered
        }}</el-tag>
      </div>
      <div>
        答对:<el-tag type="success" class="ans_info">{{
          correct_answers
        }}</el-tag>
      </div>
      <div>
        答错:<el-tag type="danger" class="ans_info">{{
          total_answered - correct_answers
        }}</el-tag>
      </div>
    </div>
    <div class="calc_box_text">
      <div class="calc_box_expression">{{ expression }}</div>
      <div class="calc_box_answer">
        <el-button>Default</el-button>
        <el-button type="primary">Primary</el-button>
        <el-button type="success">Success</el-button>
        <el-button type="info">Info</el-button>
        <el-button type="warning">Warning</el-button>
        <el-button type="danger">Danger</el-button>
      </div>
    </div>
  </el-row>
</template>

<style>
.calc_box_expression {
  background-color: blueviolet;
  font-size: 20px;
  font-weight: 600;
  height: 60px;
}

.ans_info {
  font-size: 15px;
  font-weight: 600;
  height: 60px;
}
.calc_box {
  /* background-color: rgb(251, 243, 193); */
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  height: 500px;
  gap: 20px;
}

.calc_box_text {
  background-color: rgb(30, 206, 88);
  font-size: 20px;
  font-weight: 600;
  text-align: center;
  height: 400px;
  width: 1000px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.calc_box_info {
  /* background-color: rgb(255, 166, 0); */
  font-size: 20px;
  font-weight: 600;
  text-align: center;
  height: 100px;
  width: 1000px;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
  margin-bottom: 20px;
  gap: 40px;
}

.select_point_text {
  font-size: 20px;
  font-weight: 600;
  text-align: center;
}

.el-input--large {
  font-size: 20px;
}
.el-input__wrapper {
  height: 35px;
}
.el-select__wrapper {
  height: 30px;
}

.el-option__label {
  font-size: 16px;
  font-weight: bold;
}
.el-input__inner {
  color: brown;
  font-size: 20px;
  height: 20px;
  line-height: 20px;
  font-weight: bold;
}

.el-cascader-node {
  height: 50px;
}
.el-cascader-node__label,
.el-select-dropdown__item {
  /* color: chartreuse; */
  font-size: 20px;
}

.el-cascader-menu__wrap.el-scrollbar__wrap {
  height: 350px;
}

.el-select__selected-item {
  color: brown;
  font-size: 20px;
  height: 35px;
  line-height: 40px;
  font-weight: bold;
}
</style>
