
from app.agent.planner import create_plan


def main():
    query = """
    分析近期 AI Agent 行业的发展情况，
    重点研究 OpenAI、Google、Anthropic 三家公司的最新进展，
    并总结未来发展趋势。
    """

    plan = create_plan(query)

    print("\n========== 研究目标 ==========")
    print(plan.goal)

    print("\n========== 研究任务 ==========")

    for task in plan.tasks:
        print(f"\n任务 {task.id}")
        print(task.description)


if __name__ == "__main__":
    main()
