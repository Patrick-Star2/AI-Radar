
import json

from openai import OpenAI
from pydantic import BaseModel, Field

from app.config.settings import settings


# 1. 定义研究任务的数据结构
class ResearchTask(BaseModel):
    id: int = Field(description="任务编号")
    description: str = Field(description="具体研究任务")


# 2. 定义完整研究计划的数据结构
class ResearchPlan(BaseModel):
    goal: str = Field(description="本次研究的总体目标")
    tasks: list[ResearchTask] = Field(
        description="需要依次执行的研究任务"
    )


# 3. 创建模型客户端
client = OpenAI(
    api_key=settings.LLM_API_KEY,
    base_url=settings.LLM_BASE_URL,
)


# 4. 定义 Planner 的系统提示词
PLANNER_PROMPT = """
你是一个专业的 AI 行业研究规划专家。

你的任务是将用户提出的研究问题拆解成具体、可执行的研究任务。

要求：
1. 明确本次研究的总体目标。
2. 将复杂问题拆解为 3 到 6 个具体任务。
3. 每个任务必须清晰、独立，并且可以通过网络搜索执行。
4. 任务之间尽量避免重复。
5. 最后一个任务可以用于综合分析和趋势总结。
6. 只输出合法 JSON，不要输出 Markdown 或其他解释。

输出格式：
{
    "goal": "研究总体目标",
    "tasks": [
        {
            "id": 1,
            "description": "具体研究任务"
        }
    ]
}
"""


# 5. 创建规划函数
def create_plan(user_query: str) -> ResearchPlan:
    response = client.chat.completions.create(
        model=settings.LLM_MODEL,
        messages=[
            {
                "role": "system",
                "content": PLANNER_PROMPT,
            },
            {
                "role": "user",
                "content": user_query,
            },
        ],
        temperature=0.3,
    )

    content = response.choices[0].message.content

    if not content:
        raise ValueError("模型没有返回规划内容")

    # 解析模型返回的 JSON
    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        raise ValueError(
            f"模型返回的内容不是合法 JSON：\n{content}"
        )

    # 使用 Pydantic 验证数据结构
    plan = ResearchPlan.model_validate(data)

    if not 3 <= len(plan.tasks) <= 6:
        raise ValueError("研究任务数量应在 3 到 6 个之间")

    return plan
