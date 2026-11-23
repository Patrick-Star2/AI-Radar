
from app.tools.embedding import get_embedding
from app.tools.similarity import cosine_similarity


def main():
    text_a = "Google Gemini Agent 商业化应用案例"
    text_b = "Google Gemini Agent business use cases"

    vector_a = get_embedding(text_a)
    vector_b = get_embedding(text_b)

    similarity = cosine_similarity(vector_a, vector_b)

    print("搜索词 A：", text_a)
    print("搜索词 B：", text_b)

    print("向量 A 维度：", len(vector_a))
    print("向量 B 维度：", len(vector_b))

    print("余弦相似度：", round(similarity, 4))


if __name__ == "__main__":
    main()
