<script setup>
import { ref } from "vue";
import { ElMessage } from "element-plus";

const gutterSize = ref(10);
const value = ref([]); // 年级选择器绑定值
const levelValue = ref(""); // 知识点选择器绑定值
// 关键修复：重新定义 isLoading 响应式变量
const isLoading = ref(false);

// 知识点选项（一级结构）
const options_level = ref([]);

const total_answered = ref(0);
const correct_answers = ref(0);
const current_problem_id = ref(1);

const expression = ref("等待出题");
const answer = ref(0);
const userInput = ref("");
const wrong_answers = ref([]);

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
          { value: "4", label: "下册", disabled: true },
        ],
      },
      {
        value: "grade3",
        label: "三年级",
        disabled: true,
        children: [
          { value: "5", label: "上册", disabled: true },
          { value: "6", label: "下册", disabled: true },
        ],
      },
      {
        value: "grade4",
        label: "四年级",
        disabled: true,
        children: [
          { value: "7", label: "上册", disabled: true },
          { value: "8", label: "下册", disabled: true },
        ],
      },
      {
        value: "grade5",
        label: "五年级",
        disabled: true,
        children: [
          { value: "9", label: "上册", disabled: true },
          { value: "10", label: "下册", disabled: true },
        ],
      },
      {
        value: "grade6",
        label: "六年级",
        disabled: true,
        children: [
          { value: "11", label: "上册", disabled: true },
          { value: "12", label: "下册", disabled: true },
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
        value: `${level.id}`,
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

// 检查答案
const checkAnswer = () => {
  total_answered.value++;
  // console.log(userInput.value);
  // console.log(answer.value);
  if (parseInt(userInput.value) == answer.value) {
    ElMessage({
      message: "回答正确太棒了！！！",
      type: "success",
    });
    correct_answers.value++;
    userInput.value = "";
    get_question(levelValue.value);
  } else {
    ElMessage({
      message: "回答错误，请重新输入",
      type: "error",
    });

    wrong_answers.value.push(expression.value + userInput.value);
    userInput.value = "";
  }
};
</script>

<template>
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
      <div class="calc_box_expression">
        {{ expression }}
        <!-- 增加自定义类名custom-input -->
        <input
          v-if="expression !== '等待出题'"
          type="text"
          v-model="userInput"
          placeholder="请输入答案"
          class="custom-input"
          @keyup.enter="checkAnswer"
        />
        <el-button
          v-if="expression !== '等待出题'"
          type="primary"
          style="height: 100px; width: 150px; margin-left: 20px"
          @click="checkAnswer"
          >确认</el-button
        >
      </div>
      <div class="calc_box_wrong">错题记录：{{ wrong_answers.join("，") }}</div>
    </div>
  </el-row>
</template>

<style>
.calc_box_wrong {
  margin-top: 20px;
  height: 200px;
  width: 1000px;
  background-color: lightcyan;
  font-size: 20px;
  font-weight: 600;
  color: red;
  text-align: left;
}
.calc_box_answer {
  margin-top: 20px;
}
/* 占位符样式（可选） */
.custom-input::placeholder {
  color: grey; /* 半透明白色，更柔和 */
  font-size: 32px; /* 占位符字体稍小 */
}
.custom-input {
  font-size: 150px; /* 和表达式字体大小一致 */
  font-weight: 600;
  color: grey; /* 字体颜色和背景对比 */
  background: transparent; /* 透明背景，融入父容器 */
  border: none; /* 去掉默认边框 */
  border-bottom: 2px solid grey; /* 仅保留下划线 */
  outline: none; /* 去掉聚焦时的默认外框 */
  width: 200px; /* 限制输入框宽度 */
  padding: 5px 0; /* 上下内边距，优化点击区域 */
  text-align: center; /* 输入内容居中 */
}
.calc_box_expression {
  background-color: azure;
  font-size: 150px;
  font-weight: 600;
  height: 200px;
  gap: 20px;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  color: grey;
  width: 1300px;
}

.ans_info {
  font-size: 15px;
  font-weight: 600;
  height: 60px;
}
.calc_box {
  /* background-color: rgb(251, 243, 193); */
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 700px;
  gap: 10px;
}

.calc_box_text {
  background-color: rgb(255, 255, 255);
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
  height: 80px;
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
