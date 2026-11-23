
from app.tools.embedding import get_embedding


def main():
    text = "Google Gemini Agent 商业化应用案例"

    vector = get_embedding(text)

    print("文本：", text)
    print("向量维度：", len(vector))
    print("向量前 5 个值：", vector[:5])


if __name__ == "__main__":
    main()
