# GaliLeo AI | 智能简历分析系统

系统通过 AI 技术实现简历的自动化解析、结构化信息提取以及针对招聘岗位的精准评分匹配。

## 🔗 项目链接
* **线上演示地址 (GitHub Pages)**: [https://123321-cnmb.github.io/sidereus-resume-ai/]
* **后端 API 地址 (阿里云 FC)**: `https://resume-api-sidereus-ai-cstsngiwez.cn-hangzhou.fcapp.run`
* **GitHub 仓库**: [(https://github.com/123321-cnmb/sidereus-resume-ai.git)]

---

## 🏗️ 项目架构与技术选型

本项目采用前后端分离的**分层架构**设计，并针对 Serverless 环境进行了针对性优化。

### 1. 后端技术栈 (Python 3.10 + FastAPI)
* **核心框架**: FastAPI (高性能异步 RESTful 接口)
* **大模型驱动**: DeepSeek Chat API (基于 JSON Mode 实现高可靠结构化输出)
* **解析引擎**: `pdfplumber` (多页 PDF 文本精准提取) + 正则表达式清洗
* **数据校验**: Pydantic v2 (严格定义 Resume 模型，确保 LLM 输出数据的稳定性)
* **缓存机制**: 基于内存的 MD5 哈希缓存，避免相同简历与 JD 的重复计算

### 2. 前端技术栈 (Vanilla JS + Glassmorphism UI)
* **交互体验**: 原生 JavaScript 驱动，无框架依赖，实现极速加载
* **UI 设计**: 采用毛玻璃（Glassmorphism）质感 UI，配合 Lucide 图标库与 Shimmer 加载动画
* **响应式**: 支持 PC 端与移动端的基础适配

### 3. 工程化与部署
* **代码结构**: 严格遵循分层模式（api, core, models, services, prompts）
* **Serverless**: 部署于阿里云函数计算 (FC)，通过 `a2wsgi` 适配 WSGI 协议
* **CI/CD**: 通过 GitHub Pages 托管静态前端，实现全链路公网可访问

---

## 📂 项目目录说明
```text
.
├── api/                # 路由层：处理请求分发
├── core/               # 配置层：全局设置与缓存管理
├── models/             # 模型层：Pydantic 数据结构定义
├── services/           # 业务逻辑层：LLM 调用与 PDF 解析引擎
├── prompts/            # 提示词层：HR 视角 AI 提示词模板 (Markdown)
├── index.html          # 前端单页面
├── main.py             # 阿里云 FC 挂载入口
├── s.yaml              # Serverless 部署配置文件
└── requirements.txt    # 依赖声明

## 🛠️ 部署说明

### 1. 后端部署 (阿里云 函数计算 FC)
项目针对 Serverless 架构进行了优化，支持通过 `Serverless Devs` 工具一键发布：
1. **环境准备**：安装 `Aliyun Serverless Devs` 工具并配置凭据（AccessKey）。
2. **依赖安装**：在本地执行 `pip install -r requirements.txt -t .`（FC 运行环境需携带依赖，本项目已通过 `.gitignore` 确保代码库整洁）。
3. **一键部署**：
   ```bash
   s deploy
   ```
4. **环境变量**：在阿里云控制台配置 `MY_REAL_API_KEY` 环境变量，指向 DeepSeek API Key。

### 2. 前端部署 (GitHub Pages)
1. 将 `index.html` 中的 `fetch` 请求地址修改为部署后的 FC 触发器 URL。
2. 在 GitHub 仓库设置中开启 **Pages** 服务，选择 `main` 分支根目录发布即可。

---

## 📖 使用说明

1. **访问界面**：打开线上演示地址，进入 GaliLeo AI 交互界面。
2. **上传简历**：点击或拖拽一个 **PDF 格式** 的简历文件（支持多页）。
3. **输入需求**：在输入框内填入目标岗位的描述（JD），例如“Python 后端，熟悉 FastAPI，有 AI 项目经验”。
4. **获取分析**：
   * 点击“开始深度分析”，系统将进行 PDF 解析 -> 文本清洗 -> LLM 结构化提取 -> 岗位匹配计算。
   * **输出结果**：页面将实时展示综合得分、HR 评价、候选人关键信息及重点项目经历。
5. **缓存机制说明**：若上传相同的简历与 JD，系统将触发 **INSTANT MATCH** 标签，直接从内存缓存返回结果。

---

## 🌟 已实现功能 & 加分项
- [x] **必选**：支持单个 PDF 上传与多页文本解析清洗。
- [x] **必选**：利用大模型提取姓名、电话、邮箱、地址等基础信息。
- [x] **加分项**：自动提取求职意向、期望薪资、工作年限、学历背景。
- [x] **加分项**：基于 AI 模型对候选人进行技能、经验相关性的多维度精准评分。
- [x] **加分项**：实现 MD5 缓存机制，极大降低了重复请求的响应时间与 Token 消耗。
- [x] **加分项**：采用解耦的**分层工程架构**，大幅提升了项目的可测试性与代码质量。


