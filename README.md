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
