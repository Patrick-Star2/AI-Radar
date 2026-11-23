
"""
AI Radar Embedding 模型对比实验数据集

label:
1 = 两个搜索词表达相同或高度重叠的研究意图
0 = 两个搜索词研究方向不同，不应该去重
"""

TEST_PAIRS = [
    # 正样本：相同研究意图
    {
        "query_a": "Google Gemini Agent 商业化应用案例",
        "query_b": "Google Gemini Agent business use cases",
        "label": 1,
        "category": "商业化",
    },
    {
        "query_a": "OpenAI Responses API 的工具调用能力",
        "query_b": "OpenAI Responses API function calling and tool use",
        "label": 1,
        "category": "产品能力",
    },
    {
        "query_a": "Anthropic MCP 协议的核心机制",
        "query_b": "MCP protocol architecture and how it works",
        "label": 1,
        "category": "技术协议",
    },
    {
        "query_a": "Google Jules 编程 Agent 的功能",
        "query_b": "Jules by Google coding agent features",
        "label": 1,
        "category": "产品能力",
    },
    {
        "query_a": "OpenAI Operator 浏览器自动化能力",
        "query_b": "OpenAI Operator browser automation capabilities",
        "label": 1,
        "category": "产品能力",
    },
    {
        "query_a": "企业部署 AI Agent 的投资回报率",
        "query_b": "AI Agent enterprise deployment ROI",
        "label": 1,
        "category": "商业化",
    },

    # 负样本：相关但研究意图不同
    {
        "query_a": "Google Astra 的实时语音交互能力",
        "query_b": "Google Gemini Enterprise 的产品定价",
        "label": 0,
        "category": "不同研究方向",
    },
    {
        "query_a": "Anthropic MCP 协议的技术架构",
        "query_b": "Claude Computer Use 的安全风险",
        "label": 0,
        "category": "不同研究方向",
    },
    {
        "query_a": "OpenAI AgentKit 的开发工具能力",
        "query_b": "OpenAI 公司的年度营收增长",
        "label": 0,
        "category": "不同研究方向",
    },
    {
        "query_a": "Devin 编程 Agent 的融资情况",
        "query_b": "Cursor IDE 的代码补全功能",
        "label": 0,
        "category": "不同研究方向",
    },
    {
        "query_a": "Google A2A Agent 通信协议",
        "query_b": "Google Gemini 模型基准测试成绩",
        "label": 0,
        "category": "不同研究方向",
    },
    {
        "query_a": "AI Agent 提示词注入安全风险",
        "query_b": "AI Agent 创业公司的融资情况",
        "label": 0,
        "category": "不同研究方向",
    },
    # 正样本：相同研究意图
    {
        "query_a": "Claude Code 的核心功能和使用方法",
        "query_b": "Claude Code key features and how to use it",
        "label": 1,
        "category": "产品能力"
    },
    {
        "query_a": "OpenAI Operator 的实际应用场景",
        "query_b": "Operator by OpenAI real-world use cases",
        "label": 1,
        "category": "应用场景"
    },
    {
        "query_a": "AI Agent 长期记忆的技术原理",
        "query_b": "AI Agent long-term memory architecture",
        "label": 1,
        "category": "技术原理"
    },
    {
        "query_a": "企业使用 AI Agent 的成本收益分析",
        "query_b": "企业 AI Agent 部署的 ROI 分析",
        "label": 1,
        "category": "商业化"
    },
    {
        "query_a": "Google Gemini 多模态能力介绍",
        "query_b": "Gemini multimodal capabilities overview",
        "label": 1,
        "category": "产品能力"
    },
    {
        "query_a": "MCP 协议如何连接 AI 模型与外部工具",
        "query_b": "How MCP connects AI models with external tools",
        "label": 1,
        "category": "技术协议"
    },
    {
        "query_a": "AI Agent 工作流编排框架对比",
        "query_b": "Comparison of AI Agent orchestration frameworks",
        "label": 1,
        "category": "技术比较"
    },
    {
        "query_a": "Anthropic Claude 的企业市场布局",
        "query_b": "Anthropic Claude enterprise market strategy",
        "label": 1,
        "category": "商业化"
    },
    {
        "query_a": "AI 编程 Agent 的代码生成能力",
        "query_b": "AI coding agents code generation capabilities",
        "label": 1,
        "category": "产品能力"
    },

    # 负样本：不同研究意图
    {
        "query_a": "Google Jules 编程 Agent 的产品功能",
        "query_b": "Google Astra 实时语音交互技术",
        "label": 0,
        "category": "不同产品"
    },
    {
        "query_a": "MCP 协议的技术架构",
        "query_b": "MCP 协议的商业化应用案例",
        "label": 0,
        "category": "不同研究方向"
    },
    {
        "query_a": "Claude Code 的代码生成能力",
        "query_b": "Claude Code 的订阅价格和收费模式",
        "label": 0,
        "category": "不同研究方向"
    },
    {
        "query_a": "OpenAI 模型训练技术",
        "query_b": "OpenAI 公司年度营收和利润",
        "label": 0,
        "category": "不同研究方向"
    },
    {
        "query_a": "AI Agent 的记忆管理技术",
        "query_b": "AI Agent 的安全和权限控制",
        "label": 0,
        "category": "不同研究方向"
    },
    {
        "query_a": "Google Gemini 模型的推理性能",
        "query_b": "Google Gemini 产品的商业化定价",
        "label": 0,
        "category": "不同研究方向"
    },
    {
        "query_a": "AI 编程 Agent 的融资和估值情况",
        "query_b": "AI 编程 Agent 的代码补全准确率",
        "label": 0,
        "category": "不同研究方向"
    },
    {
        "query_a": "Anthropic MCP 协议的安全机制",
        "query_b": "Anthropic 公司的市场份额和竞争格局",
        "label": 0,
        "category": "不同研究方向"
    },
    {
        "query_a": "AI Agent 多智能体协作机制",
        "query_b": "AI Agent 创业公司的融资趋势",
        "label": 0,
        "category": "不同研究方向"
    },
]


if __name__ == "__main__":
    print(f"测试数据总数：{len(TEST_PAIRS)}")

    positive_count = sum(
        1 for item in TEST_PAIRS if item["label"] == 1
    )
    negative_count = sum(
        1 for item in TEST_PAIRS if item["label"] == 0
    )

    print(f"正样本数量：{positive_count}")
    print(f"负样本数量：{negative_count}")

    for index, item in enumerate(TEST_PAIRS, start=1):
        print(
            f"{index}. [{item['label']}] "
            f"{item['query_a']}  <->  {item['query_b']}"
        )
