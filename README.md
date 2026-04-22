# GaliLeo AI | 智能简历分析系统

系统通过 AI 技术实现简历的自动化解析、结构化信息提取以及针对招聘岗位的精准评分匹配。

## 🔗 项目链接
* **线上演示地址**: [https://123321-cnmb.github.io/sidereus-resume-ai/](https://123321-cnmb.github.io/sidereus-resume-ai/)
* **后端 API 地址**: `https://resume-api-sidereus-ai-cstsngiwez.cn-hangzhou.fcapp.run`
* **GitHub 仓库**: [https://github.com/123321-cnmb/sidereus-resume-ai](https://github.com/123321-cnmb/sidereus-resume-ai)

---

## 🏗️ 项目架构与技术选型

本项目采用前后端分离的**分层架构**设计，并针对 Serverless 环境进行了针对性优化。

### 1. 后端技术栈 (Python 3.10 + FastAPI)
* **核心框架**: FastAPI (高性能异步 RESTful 接口)
* **大模型驱动**: DeepSeek Chat API (基于 JSON Mode 实现高可靠结构化输出)
* **解析引擎**: `pdfplumber` (多页 PDF 文本精准提取) + 正则表达式清洗
* **数据校验**: Pydantic v2 (严格定义 Resume 模型，确保 LLM 输出稳定性)
* **缓存机制**: 基于内存的 MD5 哈希缓存，有效规避重复计算

### 2. 前端技术栈 (Vanilla JS + Glassmorphism UI)
* **交互体验**: 原生 JavaScript 驱动，无框架依赖，秒级加载响应
* **UI 设计**: 采用毛玻璃（Glassmorphism）质感 UI，配合 Lucide 图标与 Shimmer 加载动画
* **响应式**: 支持 PC 端与移动端的基础适配

### 3. 工程化与部署
* **代码结构**: 严格遵循分层模式（api, core, models, services, prompts）
* **Serverless**: 部署于阿里云函数计算 (FC)，通过 `a2wsgi` 适配
* **CI/CD**: GitHub Pages 自动部署，实现全链路公网访问

---

## 📂 项目目录说明
```text
.
├── api/                # 路由层：处理接口请求分发
├── core/               # 配置层：环境设置与缓存管理
├── models/             # 模型层：数据结构定义 (Pydantic)
├── services/           # 业务层：LLM 逻辑与 PDF 解析引擎
├── prompts/            # 提示词层：Markdown 格式提示词模板
├── index.html          # 前端单页面入口
├── main.py             # 程序入口 & 阿里云 FC 适配
├── s.yaml              # Serverless Devs 配置文件
└── requirements.txt    # 依赖包清单
```

---

## 🛠️ 部署说明

### 1. 后端部署 (阿里云函数计算 FC)
项目支持通过 `Serverless Devs` 工具一键发布：
1. **环境准备**: 安装 Serverless Devs 并配置阿里云凭据。
2. **依赖处理**: 本地执行 `pip install -r requirements.txt -t .` 以打包运行环境。
3. **执行发布**: 
   ```bash
   s deploy
   ```
4. **环境变量**: 在 FC 控制台配置 `MY_REAL_API_KEY` 指向 DeepSeek API Key。

### 2. 前端部署 (GitHub Pages)
1. 确保 `index.html` 中的 `fetch` 地址指向已发布的 FC API。
2. 在仓库 **Settings -> Pages** 中开启服务，选择 `main` 分支发布。

---

## 📖 使用说明

1. **访问界面**: 打开线上演示地址进入交互中心。
2. **上传简历**: 点击或拖拽 **PDF 格式** 简历文件。
3. **输入需求**: 填入岗位描述（如：Python 开发，熟悉大模型调用）。
4. **获取分析**:
   * 点击“开始深度分析”，系统进行：PDF 解析 -> 文本清洗 -> LLM 提取 -> 精准打分。
   * **结果展示**: 实时反馈综合得分、HR 评价及结构化个人信息。
5. **缓存提示**: 相同输入将触发 **INSTANT MATCH** 标识，实现毫秒级响应。

---

## 🌟 已实现功能 
- [x] **必选模块**: 支持多页 PDF 文本解析、清洗与上传。
- [x] **必选模块**: 结构化提取姓名、电话、邮箱、地址等基础信息。
- [x] **加分项**: 深度提取求职意向、期望薪资、工作年限、项目经历。
- [x] **加分项**: 基于 AI 实现技能与经验相关性的多维度精准打分。
- [x] **加分项**: 内存级 MD5 缓存机制，极大优化 Token 消耗与响应速度。
- [x] **加分项**: 标准**分层工程架构**，代码高内聚低耦合，符合工程化规范。

---
