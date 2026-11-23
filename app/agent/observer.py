
from openai import OpenAI
import json

from app.config.settings import settings


client = OpenAI(
    api_key=settings.LLM_API_KEY,
    base_url=settings.LLM_BASE_URL
)


def observe_results(task_description: str, search_result: dict):
    """
    分析搜索结果，判断信息是否充分。
    """

    prompt = f"""
你是一名 AI 行业研究员。

请分析下面的研究任务和搜索结果。

研究任务：
{task_description}

搜索结果：
{json.dumps(search_result, ensure_ascii=False, indent=2)}

请判断：
1. 搜索结果是否与研究任务相关？
2. 已经获得了哪些有效信息？
3. 还缺少哪些关键信息？
4. 是否需要继续搜索？
5. 必须参考之前已经执行过的搜索内容。
6. 不要重复提出已经搜索过或高度相似的关键词。
7. 如果某个方向已经搜索但信息仍然不足，
   应尝试更换搜索角度或寻找官方文档。
8. 优先补充尚未覆盖的研究方向，
   不要反复集中搜索同一个方向。
请严格按照以下 JSON 格式返回：
{{
    "is_sufficient": true,
    "found_information": [
        "已经找到的信息"
    ],
    "missing_information": [
        "仍然缺少的信息"
    ],
    "suggested_queries": [
        "建议补充搜索的关键词"
    ],
    "reason": "判断理由"
}}

注意：
- is_sufficient 必须是 true 或 false。
- 如果信息不足，suggested_queries 应提供具体搜索关键词。
- 不要编造搜索结果中不存在的事实。
"""

    response = client.chat.completions.create(
        model=settings.LLM_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        response_format={"type": "json_object"}
    )

    return json.loads(response.choices[0].message.content)
