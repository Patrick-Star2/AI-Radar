
import math


def cosine_similarity(
    vector_a: list[float],
    vector_b: list[float]
) -> float:
    """
    计算两个向量的余弦相似度。
    """

    if len(vector_a) != len(vector_b):
        raise ValueError("两个向量的维度必须一致")

    if not vector_a:
        raise ValueError("向量不能为空")

    dot_product = sum(
        a * b for a, b in zip(vector_a, vector_b)
    )

    norm_a = math.sqrt(sum(a * a for a in vector_a))
    norm_b = math.sqrt(sum(b * b for b in vector_b))

    if norm_a == 0 or norm_b == 0:
        raise ValueError("不能计算零向量的相似度")

    return dot_product / (norm_a * norm_b)