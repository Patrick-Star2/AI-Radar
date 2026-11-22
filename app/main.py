from app.agent.core import run_agent


def main():

    print("=" * 50)
    print("       Welcome to AI Radar")
    print("       AI Intelligence Agent")
    print("=" * 50)
    #多轮对话循环
    while True:

        user_input = input(
            "\n请输入你的研究问题（输入 exit 退出）：\n> "
        ).strip()
        #退出
        if user_input.lower() == "exit":
            print("AI Radar 已退出")
            break

        if not user_input:
            continue

        try:
            #调用agent执行用户的提问
            result = run_agent(user_input)

            print("\n" + "=" * 50)
            print("AI Radar 研究结果")
            print("=" * 50)
            print(result)

        except Exception as e:
            print(f"\n执行失败：{e}")


if __name__ == "__main__":
    main()