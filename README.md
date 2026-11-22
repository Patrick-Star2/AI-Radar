# AI Radar

**一个基于大语言模型的 AI 行业情报研究 Agent**

AI Radar 是一个使用 Python 开发的 AI 行业情报研究项目，目标是构建一个能够自主搜索、收集、整理和分析 AI 行业信息的智能 Agent。

项目希望让 AI 不仅能够回答问题，还能够主动调用外部工具获取信息，并在此基础上完成研究任务，最终生成结构化的行业分析报告。

目前项目处于基础 Agent 开发阶段，采用 Single Agent 架构，逐步实现从基础模型调用到自主研究系统的完整能力。

---

## 一、项目目标

AI Radar 希望逐步实现以下能力：

- **自主理解问题**：理解用户提出的 AI 行业研究需求。
- **信息搜索**：调用搜索工具获取最新的 AI 行业信息。
- **信息整理**：提取新闻、技术进展、企业动态等关键信息。
- **信息分析**：识别重要事件，分析行业影响和发展趋势。
- **报告生成**：输出结构化研究报告，并保留信息来源。
- **持续进化**：逐步引入规划、记忆、多 Agent 协作和自动化研究能力。

最终目标是构建一个能够持续追踪 AI 行业动态的智能研究助手。

## 二、技术栈

| 技术 | 用途 |
|---|---|
| Python 3.11 / 3.12 | 项目主要开发语言 |
| 阿里云百炼 Qwen | 大语言模型服务 |
| OpenAI Python SDK | 通过兼容接口调用模型 |
| Tavily | 网络信息搜索 |
| Pydantic | 数据结构与参数校验 |
| python-dotenv | 环境变量管理 |
| Git / GitHub | 版本管理与代码托管 |

说明：项目使用 OpenAI 兼容 SDK 接口调用模型，不代表使用 OpenAI 自有模型。

## 三、项目结构

```text
ai-radar/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── agent/
│   │   ├── __init__.py
│   │   ├── core.py
│   │   └── prompts.py
│   │
│   ├── tools/
│   │   ├── __init__.py
│   │   └── search.py
│   │
│   └── config/
│       ├── __init__.py
│       └── settings.py
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

### 核心模块说明

- `app/main.py`：项目命令行入口，负责接收用户输入并启动 Agent。
- `app/agent/core.py`：Agent 核心逻辑，负责模型调用、工具选择和工具执行循环。
- `app/agent/prompts.py`：定义 Agent 的角色、任务要求和输出规范。
- `app/tools/search.py`：封装 Tavily 网络搜索能力。
- `app/config/settings.py`：统一管理模型和搜索服务的环境配置。
- `.env`：保存本地 API Key 和服务配置。
- `.env.example`：环境变量配置模板。
- `requirements.txt`：项目依赖清单。

## 四、运行环境

建议使用以下环境：

- Python 3.11 或更高版本
- PyCharm
- Git
- 阿里云百炼 API Key
- Tavily API Key

## 五、安装与运行

### 1. 克隆项目

```bash
git clone 你的GitHub仓库地址
cd ai-radar
```

### 2. 创建虚拟环境

```bash
python -m venv .venv
```

Windows PowerShell 激活环境：

```powershell
.venv\Scripts\Activate.ps1
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 配置环境变量

复制 `.env.example`，创建 `.env` 文件，并填写自己的服务配置：

```env
LLM_API_KEY=你的百炼API_KEY
LLM_BASE_URL=你的百炼兼容接口地址
LLM_MODEL=qwen4-max
TAVILY_API_KEY=你的Tavily_API_KEY
```

注意：`LLM_BASE_URL` 应根据百炼账号的计费方案、地域和接口配置填写。

### 5. 启动项目

```bash
python -m app.main
```

启动后，可以在命令行输入研究问题，例如：

```text
分析近期 AI Agent 行业的重要进展，并总结未来发展趋势。
```

## 六、当前开发进度

| 功能 | 当前状态 |
|---|---|
| Python 项目基础结构 | 已完成 |
| 环境变量配置 | 已完成 |
| 大语言模型 API 接入 | 第一阶段 |
| Tavily 搜索工具封装 | 第一阶段 |
| Agent 基础循环 | 第一阶段 |
| Function Calling | 第一阶段 |
| 自主任务规划 | 待开发 |
| 多 Agent 协作 | 待开发 |
| 长期记忆与 RAG | 待开发 |
| 信息事实核查 | 待开发 |
| 定时自动研究 | 待开发 |
| Web 可视化界面 | 待开发 |

注：这里的进度应以实际运行测试结果为准，完成代码编写不等于所有功能已经验证通过。

## 七、未来开发规划

AI Radar 计划分阶段演进：

**Phase 1：基础 Agent**

搭建 Python 项目结构，实现模型调用、工具调用和基础 Agent 执行循环。

**Phase 2：自主规划与推理**

引入 Planning、ReAct 等机制，让 Agent 能够拆解复杂研究任务，并根据搜索结果调整行动。

**Phase 3：Multi-Agent 多智能体架构**

拆分新闻搜索、技术研究、企业分析和报告生成等角色，实现多 Agent 协作。

**Phase 4：Memory & RAG**

建立长期记忆和知识库，让 Agent 能够积累历史研究资料，并进行关联分析。

**Phase 5：信息核查与质量评估**

增加多来源交叉验证、事实核查和研究结果评估机制，提高报告可信度。

**Phase 6：自动化研究**

支持定时执行研究任务，持续追踪 AI 行业动态。

**Phase 7：Web UI**

搭建可视化界面，让用户能够提交研究任务、查看研究过程和阅读分析报告。

## 八、项目开发理念

本项目采用边学习、边开发的方式推进。

开发过程中重点关注：

1. 理解 Agent 的底层工作机制，而不是只依赖框架。
2. 优先使用原生 Python 实现核心逻辑。
3. 理解模型、工具、上下文和执行循环之间的关系。
4. 每个阶段都进行独立测试和版本提交。
5. 逐步提升系统的稳定性、可扩展性和研究质量。

## 九、安全说明

- `.env` 文件包含敏感 API Key，禁止上传到 GitHub。
- `.env.example` 只保留配置项，不填写真实密钥。
- 不要将 API Key 硬编码在 Python 源代码中。
- 如果密钥意外公开，应及时撤销并重新生成。

## 十、项目定位

AI Radar 不只是一个 AI 新闻搜索工具。

它希望逐步进化为一个能够自主发现问题、规划研究路径、调用工具、分析信息并形成结论的 AI 行业研究 Agent。

**让 AI 不只是回答问题，而是具备自主研究和分析信息的能力。**

---

**Project Status:** In Development

**Language:** Python

**Project Type:** AI Agent / AI Industry Research