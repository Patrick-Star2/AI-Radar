
from app.agent.executor import execute_plan
from app.agent.observer import observe_results


if __name__ == "__main__":

    query = "分析近期 AI Agent 行业的发展趋势"

    # 第一步：生成计划并执行搜索
    execution_result = execute_plan(query)

    # 第二步：观察每个任务的搜索结果
    for item in execution_result["results"]:

        print("\n========== Observer 分析 ==========")

        observation = observe_results(
            task_description=item["task_description"],
            search_result=item["search_result"]
        )

        print(observation)
