# 平台服务信息文档

## 概述

本文档记录了平台中所有可用的微服务和元应用信息，包括服务的基本信息、技术规范、API接口等详细内容。

**所有采用相对路径的服务api端点，Base url均为`https://fdueblab.cn`**

## 服务列表

### 1. 样例报告生成微服务

**基本信息**
- **服务ID**: 01a951d1-09b1-4d65-9f6c-cf048e5f620e
- **服务名称**: 样例报告生成微服务
- **服务属性**: 非智能服务 (non_intelligent)
- **服务类型**: 原子服务 (atomic)
- **应用领域**: 反洗钱 (aml)
- **状态**: 预发布未评级 (pre_release_unrated)
- **编号**: 2330

**技术规范**
- **网络**: bridge
- **端口映射**: 0.0.0.0:8002/TCP → 0.0.0.0:80002
- **数据卷**: /var/opt/gitlab/mnt/user → /appdata/aml/data

**服务提供方**
- **公司名称**: 复旦大学课题组
- **地址**: 上海市杨浦区邯郸路220号
- **联系方式**: 021-65642222
- **服务介绍**: 简易版报告生成

**API接口**
1. **getReportData** (GET)
   - 路径: https://myApiServer.com/report/get
   - 参数: reportId (int)
   - 功能: 获取报告数据

2. **generateReport** (POST)
   - 路径: https://myApiServer.com/report-generation/generate
   - 参数: reportData (string)
   - 功能: 报告生成接口样例

3. **sendReport** (GET)
   - 路径: https://myApiServer.com/report/send
   - 参数: reportId (int)
   - 功能: 发送报告

---

### 2. 异常识别微服务

**基本信息**
- **服务ID**: 1f464c6b-6b49-4fa2-8ec9-6942815f7d8f
- **服务名称**: 异常识别微服务
- **服务属性**: 开源服务 (open_source)
- **服务类型**: 原子服务 (atomic)
- **应用领域**: 反洗钱 (aml)
- **状态**: 部署中 (deploying)
- **编号**: 3

**技术规范**
- **网络**: bridge
- **端口映射**: 0.0.0.0:8004/TCP → 0.0.0.0:80004
- **数据卷**: /var/opt/gitlab/mnt/user → /appdata/aml/data

**可信评估指标**
- 鲁棒性 (robustness): 5分
- 隐私保护 (privacy): 5分
- 安全指纹 (safety-fingerprint): 5分

**服务提供方**
- **公司名称**: 复旦大学课题组
- **服务介绍**: 课题五AI技术中台上传、发布算法样例服务

**API接口**
1. **visualize** (POST) - 可视化
2. **preprocess** (POST) - 数据预处理
3. **evaluate** (POST) - 模型评估
4. **predict** (POST) - 预测
5. **train** (POST) - 模型训练

---

### 3. 课题一风险识别模型推理微服务

**基本信息**
- **服务ID**: 3b3d4e4d-36e4-4436-bea1-63af2117d0bc
- **服务名称**: 课题一风险识别模型推理微服务
- **服务属性**: 开源服务 (open_source)
- **服务类型**: 原子服务 (atomic)
- **应用领域**: 反洗钱 (aml)
- **状态**: 已发布 (released)
- **编号**: 512

**技术规范**
- **网络**: ioeb_app-network
- **端口映射**: 5000/tcp → 0.0.0.0:25001 :::25001
- **数据卷**: /home/ubuntu/ioeb/api/Project_1/checkpoint -> /app/checkpoint

**可信评估指标**
- 安全指纹 (safety-fingerprint): 5分 ✓
- 隐私保护 (privacy): 5分 ✓

**服务提供方**
- **公司名称**: 复旦大学课题组
- **服务介绍**: 基于智能体的风险识别算法

**API接口**
1. **predict** (POST)
   - 路径: /api/project1/predict
   - 参数: file (zip file) - 数据集和参数配置文件的zip压缩包
   - 功能: 模型推理接口，基于数据集和参数配置得到风险识别结果

2. **healthCheck** (GET)
   - 路径: /api/project1/health
   - 功能: 判断微服务状态是否正常可用

---

### 4. 课题二多方安全计算模型推理微服务

**基本信息**
- **服务ID**: 4fda9469-dcd7-4032-affb-9c9df0cd2cc6
- **服务名称**: 课题二多方安全计算模型推理微服务
- **服务属性**: 开源服务 (open_source)
- **服务类型**: 原子服务 (atomic)
- **应用领域**: 反洗钱 (aml)
- **状态**: 已发布 (released)
- **编号**: 512

**技术规范**
- **网络**: ioeb_app-network
- **端口映射**: 5000/tcp → 0.0.0.0:25002 :::25002
- **数据卷**: /home/ubuntu/ioeb/api/Project_2/checkpoint -> /app/checkpoint

**可信评估指标**
- 安全指纹 (safety-fingerprint): 5分 ✓
- 安全水印 (safety-watermark): 5分 ✓
- 公平性 (fairness): 5分 ✓
- 隐私保护 (privacy): 5分 ✓

**服务提供方**
- **公司名称**: 复旦大学课题组
- **服务介绍**: 基于多方安全计算的风险识别算法

**API接口**
1. **predict** (POST)
   - 路径: /api/project2/predict
   - 参数: file (zip file) - 数据集和参数配置文件的zip压缩包
   - 功能: 模型推理接口，基于数据集和参数配置得到风险识别结果

2. **healthCheck** (GET)
   - 路径: /api/project2/health
   - 功能: 判断微服务状态是否正常可用

---

### 5. 技术评测元应用

**基本信息**
- **服务ID**: b1b8417a-145c-43e3-b0d1-1aa3d7279c6b
- **服务名称**: 技术评测元应用
- **服务属性**: 自定义服务 (custom)
- **服务类型**: 元应用 (meta)
- **应用领域**: 反洗钱 (aml)
- **状态**: 预发布待审 (pre_release_pending)
- **编号**: 232

**技术规范**
- **网络**: bridge
- **端口映射**: 0.0.0.0:1020/TCP → 0.0.0.0:10020
- **数据卷**: /var/opt/gitlab/mnt/user → /appdata/aml/metaApp

**可信评估指标**
- 精确度 (precision): 5分
- 召回率 (recall): 5分 ✓
- 计算效率 (computation_efficiency): 5分

**服务提供方**
- **公司名称**: 复旦大学课题组
- **服务介绍**: 用于跨境支付的风险评估和报告生成的元应用样例

**API接口**
1. **技术评测元应用** (POST)
   - 路径: https://myApiServer.com/metaApp
   - 输入名称: 技术评测数据
   - 输出名称: 技术评测报告
   - 支持输出可视化: ✓
   - 提交按钮文本: 开始评测

---

### 6. 课题三金融风险报告生成微服务

**基本信息**
- **服务ID**: b352ae47-92db-4281-8faf-9491ab6baea3
- **服务名称**: 课题三金融风险报告生成微服务
- **服务属性**: 付费服务 (paid)
- **服务类型**: 原子服务 (atomic)
- **应用领域**: 反洗钱 (aml)
- **状态**: 已发布 (released)
- **编号**: 2342

**技术规范**
- **网络**: ioeb_app-network
- **端口映射**: 5000/tcp → 0.0.0.0:25003 :::25003
- **数据卷**: /home/ubuntu/ioeb/api/Project-3/data -> /app/data

**可信评估指标**
- 鲁棒性 (robustness): 5分 ✓
- 可解释性 (explainability): 5分 ✓
- 隐私保护 (privacy): 5分 ✓

**服务提供方**
- **公司名称**: 复旦大学课题组
- **服务介绍**: 金融风险报告生成

**API接口**
1. **healthCheck** (GET)
   - 路径: /api/project3/health
   - 功能: 判断微服务状态是否正常可用

2. **generate-report** (GET)
   - 路径: /api/project3/generate-report
   - 参数: query (string) - 用自然语言描述想要生成的报告
   - 功能: 根据自然语言需求生成风险评估报告

3. **nl2gql** (GET)
   - 路径: /api/project3/nl2gql
   - 参数: query (string) - 用自然语言描述查询需求
   - 功能: 根据自然语言需求生成gql语句并得到查询结果

---

### 7. 课题四模型评测-安全性指纹微服务

**基本信息**
- **服务ID**: c482ad98-4a7b-4498-a4d5-a52f991d1c0d
- **服务名称**: 课题四模型评测-安全性指纹微服务
- **服务属性**: 付费服务 (paid)
- **服务类型**: 原子服务 (atomic)
- **应用领域**: 反洗钱 (aml)
- **状态**: 已发布 (released)
- **编号**: 2342

**技术规范**
- **网络**: ioeb_app-network
- **端口映射**: 5000/tcp → 0.0.0.0:25004 :::25004
- **数据卷**: 
  - /home/ubuntu/ioeb/api/Project-4/eval_config -> /app/eval_config
  - /home/ubuntu/ioeb/api/Project-4/eval_result -> /app/eval_result
  - /home/ubuntu/ioeb/api/Project-4/graph_dataset -> /app/graph_dataset

**可信评估指标**
- 鲁棒性 (robustness): 5分 ✓
- 隐私保护 (privacy): 5分 ✓
- 可解释性 (explainability): 5分 ✓

**服务提供方**
- **公司名称**: 复旦大学课题组
- **服务介绍**: 安全性指纹测评算法

**API接口**
1. **safety-fingerprint** (POST)
   - 路径: /api/project4/safety/safety-fingerprint
   - 参数: 
     - model_name (string) - 模型名称，目前只支持HattenGCN
     - file (file) - 数据集和配置文件的zip压缩包

2. **healthCheck** (GET)
   - 路径: /api/project4/safety/health

---

### 8. 技术评测微服务

**基本信息**
- **服务ID**: dce40ba0-b5bb-4508-bd09-38a95a2e2932
- **服务名称**: 技术评测微服务
- **服务属性**: 开源服务 (open_source)
- **服务类型**: 原子服务 (atomic)
- **应用领域**: 反洗钱 (aml)
- **状态**: 错误 (error)
- **编号**: 8192

**技术规范**
- **网络**: bridge
- **端口映射**: 0.0.0.0:8001/TCP → 0.0.0.0:80001
- **数据卷**: /var/opt/gitlab/mnt/user → /appdata/aml/data

**可信评估指标**
- 鲁棒性 (robustness): 5分 ✓
- 公平性 (fairness): 5分 ✓
- 隐私保护 (privacy): 5分 ✓

**服务提供方**
- **公司名称**: 复旦大学课题组
- **服务介绍**: 课题五样例服务

**API接口**
1. **predict** (POST)
   - 路径: https://myApiServer.com/technical-assessment/predict
   - 功能: 预测

2. **train** (POST)
   - 路径: https://myApiServer.com/technical-assessment/train
   - 功能: 模型训练

---

### 9. 信用评估微服务

**基本信息**
- **服务ID**: fde67dc7-39a2-4378-a5fe-ceec617d802f
- **服务名称**: 信用评估微服务
- **服务属性**: 付费服务 (paid)
- **服务类型**: 原子服务 (atomic)
- **应用领域**: 反洗钱 (aml)
- **状态**: 未部署 (not_deployed)
- **编号**: 42

**技术规范**
- **网络**: bridge
- **端口映射**: 0.0.0.0:8003/TCP → 0.0.0.0:80003
- **数据卷**: /var/opt/gitlab/mnt/user → /appdata/aml/data

**可信评估指标**
- 可解释性 (explainability): 5分
- 公平性 (fairness): 5分 ✓
- 隐私保护 (privacy): 5分
- 鲁棒性 (robustness): 5分 ✓

**服务提供方**
- **公司名称**: 复旦大学课题组
- **服务介绍**: 课题五样例服务

**API接口**
1. **train** (POST)
   - 路径: https://myApiServer.com/credit-assessment/train
   - 功能: 模型训练

2. **predict** (POST)
   - 路径: https://myApiServer.com/credit-assessment/predict
   - 功能: 预测

---

## 服务状态说明

- **released**: 已发布，可正常使用
- **pre_release_unrated**: 预发布未评级
- **pre_release_pending**: 预发布待审
- **deploying**: 部署中
- **error**: 服务异常
- **not_deployed**: 未部署

## 服务属性说明

- **open_source**: 开源服务
- **paid**: 付费服务
- **custom**: 自定义服务
- **non_intelligent**: 非智能服务

## 服务类型说明

- **atomic**: 原子服务
- **meta**: 元应用

## 可信评估指标说明

- **robustness**: 鲁棒性
- **privacy**: 隐私保护
- **safety-fingerprint**: 安全指纹
- **safety-watermark**: 安全水印
- **fairness**: 公平性
- **explainability**: 可解释性
- **precision**: 精确度
- **recall**: 召回率
- **computation_efficiency**: 计算效率

✓ 表示已通过平台检测
