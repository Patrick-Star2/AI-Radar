import json
from openai import OpenAI

from app.config.settings import settings
from app.tools.search import search_web
from app.agent.prompts import SYSTEM_PROMPT


settings.validate()

client = OpenAI(
    api_key=settings.LLM_API_KEY,
    base_url=settings.LLM_BASE_URL
)

#人为构造工具调用
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "search_web",
            "description": "搜索互联网，获取 AI 行业信息",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "搜索关键词"
                    }
                },
                "required": ["query"],
                "additionalProperties": False
            }
        }
    }
]


def execute_tool(name: str, arguments: dict):

    if name == "search_web":
        #获取query:xxx中的参数
        query = arguments.get("query")

        if not isinstance(query, str) or not query.strip():
            return {"error": "搜索关键词不能为空"}

        return search_web(query)

    return {
        "error": f"未知工具：{name}"
    }


def run_agent(user_input: str):
    #准备mesages,包括：SystemPrompt,humanmessage
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": user_input
        }
    ]
    #最多思考8次，避免模型一直处于搜索中
    max_steps = 8

    for step in range(max_steps):

        print(f"\n[Agent] 第 {step + 1} 轮思考")
        #暂未使用langchain、langgraph框架
        response = client.chat.completions.create(
            model=settings.LLM_MODEL,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto"
        )

        message = response.choices[0].message

        messages.append(
            message.model_dump(exclude_none=True) #过滤掉为None的字段
        )

        # 没有工具调用，返回最终结果
        if not message.tool_calls:

            print("[Agent] 任务完成")

            return message.content or ""

        # 执行工具
        for tool_call in message.tool_calls:

            name = tool_call.function.name

            print(f"[Agent] 调用工具：{name}")

            try:
                #获取要调用工具的参数
                arguments = json.loads(
                    tool_call.function.arguments
                )

                if not isinstance(arguments, dict):
                    raise ValueError("工具参数必须是 JSON 对象")

                result = execute_tool(name, arguments)

            except Exception as e:

                result = {
                    "error": str(e)
                }

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(
                    result,
                    ensure_ascii=False,
                    default=str
                )
            })

    return "已达到最大执行轮数，请缩小研究范围后重试。"