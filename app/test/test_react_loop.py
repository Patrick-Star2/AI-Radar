
from app.agent.react_loop import run_react_loop


if __name__ == "__main__":

    query = (
        "分析近期 AI Agent 行业的发展情况，"
        "重点研究 OpenAI、Google、Anthropic "
        "三家公司的最新进展，并总结未来趋势。"
    )

    result = run_react_loop(query)

    print("\n\n========== ReAct 最终执行报告 ==========")

    for item in result["results"]:

        print(f"\n研究任务：{item['task_description']}")

        print(
            "补充搜索轮数：",
            len(item["search_history"]["supplemental_searches"])
        )

        print(
            "最终信息是否充分：",
            item["final_observation"]["is_sufficient"]
        )

        print(
            "判断理由：",
            item["final_observation"]["reason"]
        )