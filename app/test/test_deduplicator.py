
from app.tools.deduplicator import SearchDeduplicator


def test_exact_duplicate():
    deduplicator = SearchDeduplicator()

    result = deduplicator.find_duplicate(
        query="OpenAI GPT-5",
        existing_queries=["openai gpt-5"]
    )

    print("\n========== 完全重复测试 ==========")
    print(result)

    assert result["is_duplicate"] is True
    assert result["method"] == "exact"


def test_empty_history():
    deduplicator = SearchDeduplicator()

    result = deduplicator.find_duplicate(
        query="OpenAI GPT-5",
        existing_queries=[]
    )

    print("\n========== 空历史记录测试 ==========")
    print(result)

    assert result["is_duplicate"] is False
    assert result["matched_query"] is None
    assert result["similarity"] == 0.0


def test_semantic_duplicate():
    deduplicator = SearchDeduplicator(threshold=0.80)

    result = deduplicator.find_duplicate(
        query="Google Gemini Agent 商业化应用案例",
        existing_queries=[
            "Google Gemini Agent business use cases"
        ]
    )

    print("\n========== 语义重复测试 ==========")
    print(result)

    assert result["is_duplicate"] is True
    assert result["method"] == "embedding"


def test_different_research_direction():
    deduplicator = SearchDeduplicator(threshold=0.80)

    result = deduplicator.find_duplicate(
        query="MCP 技术架构",
        existing_queries=[
            "MCP 商业化应用案例"
        ]
    )

    print("\n========== 不同研究方向测试 ==========")
    print(result)

    assert result["is_duplicate"] is False

if __name__ == "__main__":
    test_exact_duplicate()
    test_empty_history()
    test_semantic_duplicate()
    test_different_research_direction()

    print("\n第一轮测试全部通过！")
