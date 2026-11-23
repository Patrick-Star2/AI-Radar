
from app.agent.executor import execute_plan


if __name__ == "__main__":
    query = (
        "分析近期 AI Agent 行业的发展情况，"
        "重点研究 OpenAI、Google、Anthropic "
        "三家公司的最新进展，并总结未来趋势。"
    )

    result = execute_plan(query)

    print("\n\n========== 最终搜索结果 ==========")

    for item in result["results"]:
        print(f"\n任务：{item['task_description']}")
        print("搜索结果：")
        print(item["search_result"])
