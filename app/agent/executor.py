
from app.agent.planner import create_plan
from app.tools.search import search_web


def execute_plan(user_query: str):
    """
    根据研究计划，逐项执行搜索任务。
    """

    # 第一步：生成研究计划
    plan = create_plan(user_query)

    print("\n========== 研究目标 ==========")
    print(plan.goal)

    results = []

    # 第二步：逐项执行任务
    for task in plan.tasks:
        print(f"\n========== 执行任务 {task.id} ==========")
        print(task.description)

        # 第三步：调用 Tavily 搜索
        search_result = search_web(task.description)

        # 第四步：保存搜索结果
        results.append({
            "task_id": task.id,
            "task_description": task.description,
            "search_result": search_result
        })

    return {
        "goal": plan.goal,
        "results": results
    }
