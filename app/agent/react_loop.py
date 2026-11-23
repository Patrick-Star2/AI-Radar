
from app.agent.executor import execute_plan
from app.agent.observer import observe_results
from app.tools.search import search_web


# 每个任务最多补充搜索 2 轮
MAX_SUPPLEMENTAL_ROUNDS = 2

# 每轮最多采用 3 条补充搜索建议
MAX_QUERIES_PER_ROUND = 3


def run_react_loop(user_query: str):
    """
    运行简化版 ReAct 循环：
    计划 -> 搜索 -> 观察 -> 补充搜索 -> 再次观察
    """

    # 1. Planner 制定计划，Executor 执行初始搜索
    execution_result = execute_plan(user_query)

    final_results = []

    # 2. 每个研究任务独立执行观察和补充搜索
    for item in execution_result["results"]:

        task_id = item["task_id"]
        task_description = item["task_description"]

        print(f"\n========== ReAct 任务 {task_id} ==========")
        print(f"研究任务：{task_description}")

        # 保存初始搜索结果和后续补充搜索结果
        search_history = {
            "initial_search": item["search_result"],
            "supplemental_searches": []
        }

        # 3. 第一次观察
        observation = observe_results(
            task_description,
            search_history["initial_search"]
        )

        print("\n本轮观察结果：")
        print("信息是否充分：", observation["is_sufficient"])
        print("判断理由：", observation.get("reason"))

        print("仍然缺少的信息：")
        for info in observation.get("missing_information", []):
            print("-", info)

        print("下一轮搜索建议：")
        for query in observation.get("suggested_queries", []):
            print("-", query)

        # 4. 根据观察结果决定是否补充搜索
        for round_number in range(
            1, MAX_SUPPLEMENTAL_ROUNDS + 1
        ):

            # 信息充分，结束当前任务
            if observation.get("is_sufficient") is True:
                print("\n信息已经充分，结束当前任务。")
                break

            # 获取 Observer 提出的搜索建议
            suggested_queries = observation.get(
                "suggested_queries", []
            )

            if not isinstance(suggested_queries, list):
                suggested_queries = []

            queries = [
                query.strip()
                for query in suggested_queries
                if isinstance(query, str) and query.strip()
            ][:MAX_QUERIES_PER_ROUND]

            # 没有可用搜索建议，停止
            if not queries:
                print("\n没有有效的补充搜索建议，停止任务。")
                break

            print(f"\n========== 第 {round_number} 轮补充搜索 ==========")

            round_results = []

            for query in queries:
                print(f"\n正在搜索：{query}")

                result = search_web(query)

                round_results.append({
                    "query": query,
                    "search_result": result
                })

            # 保存本轮搜索结果
            search_history["supplemental_searches"].append({
                "round": round_number,
                "results": round_results
            })

            # 5. 将全部搜索历史交给 Observer 重新分析
            observation = observe_results(
                task_description,
                search_history
            )

            print("\n本轮观察结果：")
            print("信息是否充分：", observation["is_sufficient"])

        # 6. 保存当前任务的最终结果
        final_results.append({
            "task_id": task_id,
            "task_description": task_description,
            "search_history": search_history,
            "final_observation": observation
        })

    return {
        "goal": execution_result["goal"],
        "results": final_results
    }
