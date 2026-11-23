
VALIDATION_PAIRS = [
    # 正样本：研究意图相同
    {
        "query_a": "OpenAI GPT-5 的推理能力",
        "query_b": "GPT-5 reasoning capabilities by OpenAI",
        "label": 1,
        "category": "产品能力"
    },
    {
        "query_a": "Claude Computer Use 的工作原理",
        "query_b": "How Claude Computer Use works",
        "label": 1,
        "category": "技术原理"
    },
    {
        "query_a": "AI Agent 的任务规划机制",
        "query_b": "AI Agent task planning mechanisms",
        "label": 1,
        "category": "技术原理"
    },
    {
        "query_a": "Google Gemini Agent 的企业应用案例",
        "query_b": "Enterprise use cases of Google Gemini Agent",
        "label": 1,
        "category": "商业化"
    },
    {
        "query_a": "AI Agent 的工具调用机制",
        "query_b": "How AI agents invoke external tools",
        "label": 1,
        "category": "技术原理"
    },
    {
        "query_a": "Anthropic Claude 模型的上下文窗口",
        "query_b": "Claude model context window size",
        "label": 1,
        "category": "产品能力"
    },
    {
        "query_a": "多智能体协作系统的架构设计",
        "query_b": "Multi-agent system architecture design",
        "label": 1,
        "category": "技术架构"
    },
    {
        "query_a": "AI Agent 自动化工作流的应用",
        "query_b": "AI agent workflow automation use cases",
        "label": 1,
        "category": "应用场景"
    },
    {
        "query_a": "RAG 系统的检索优化方法",
        "query_b": "Retrieval optimization techniques for RAG systems",
        "label": 1,
        "category": "技术优化"
    },
    {
        "query_a": "AI Agent 的长期记忆存储方案",
        "query_b": "Long-term memory storage solutions for AI agents",
        "label": 1,
        "category": "技术架构"
    },

    # 负样本：研究意图不同
    {
        "query_a": "GPT-5 的推理能力测试",
        "query_b": "OpenAI 的商业收入和利润",
        "label": 0,
        "category": "不同研究方向"
    },
    {
        "query_a": "Claude Computer Use 的技术原理",
        "query_b": "Claude Computer Use 的订阅价格",
        "label": 0,
        "category": "不同研究方向"
    },
    {
        "query_a": "AI Agent 任务规划算法",
        "query_b": "AI Agent 创业公司的融资情况",
        "label": 0,
        "category": "不同研究方向"
    },
    {
        "query_a": "Google Gemini 模型的多模态能力",
        "query_b": "Google Gemini 产品的市场份额",
        "label": 0,
        "category": "不同研究方向"
    },
    {
        "query_a": "AI Agent 工具调用的技术机制",
        "query_b": "AI Agent 工具调用的安全风险",
        "label": 0,
        "category": "不同研究方向"
    },
    {
        "query_a": "Claude 模型的上下文窗口长度",
        "query_b": "Claude 模型的训练数据来源",
        "label": 0,
        "category": "不同研究方向"
    },
    {
        "query_a": "多智能体协作的通信机制",
        "query_b": "多智能体产品的商业化市场规模",
        "label": 0,
        "category": "不同研究方向"
    },
    {
        "query_a": "AI Agent 自动化工作流的技术架构",
        "query_b": "AI Agent 自动化行业的融资趋势",
        "label": 0,
        "category": "不同研究方向"
    },
    {
        "query_a": "RAG 检索准确率优化",
        "query_b": "RAG 产品的商业化定价策略",
        "label": 0,
        "category": "不同研究方向"
    },
    {
        "query_a": "AI Agent 长期记忆的存储技术",
        "query_b": "AI Agent 长期记忆的隐私安全风险",
        "label": 0,
        "category": "不同研究方向"
    },
]
