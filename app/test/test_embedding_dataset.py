
from app.tools.embedding import get_embedding
from app.tools.similarity import cosine_similarity
from app.experiments.embedding_eval.dataset import TEST_PAIRS


def main():
    positive_scores = []
    negative_scores = []

    for index, item in enumerate(TEST_PAIRS, start=1):
        query_a = item["query_a"]
        query_b = item["query_b"]
        label = item["label"]

        vector_a = get_embedding(query_a)
        vector_b = get_embedding(query_b)

        score = cosine_similarity(vector_a, vector_b)

        if label == 1:
            positive_scores.append(score)
        else:
            negative_scores.append(score)

        print(f"\n第 {index} 组")
        print("搜索词 A：", query_a)
        print("搜索词 B：", query_b)
        print("人工标签：", label)
        print("相似度：", round(score, 4))

    print("\n========== 实验汇总 ==========")

    print(
        "正样本平均相似度：",
        round(sum(positive_scores) / len(positive_scores), 4)
    )

    print(
        "负样本平均相似度：",
        round(sum(negative_scores) / len(negative_scores), 4)
    )


if __name__ == "__main__":
    main()
