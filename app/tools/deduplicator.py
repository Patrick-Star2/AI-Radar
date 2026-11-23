
import re

from app.tools.embedding import get_embedding
from app.tools.similarity import cosine_similarity


class SearchDeduplicator:
    def __init__(self, threshold: float = 0.80):
        self.threshold = threshold
        self.embedding_cache = {}

    @staticmethod
    def normalize_query(query: str) -> str:
        """标准化搜索词，处理大小写、空格和标点"""
        return re.sub(r"[\s\W_]+", "", query.lower())

    def get_cached_embedding(self, query: str) -> list[float]:
        """获取向量，优先使用缓存"""
        if query not in self.embedding_cache:
            self.embedding_cache[query] = get_embedding(query)

        return self.embedding_cache[query]

    def find_duplicate(
        self,
        query: str,
        existing_queries: list[str]
    ) -> dict:
        """
        在已有搜索词中寻找重复项。

        返回：
        is_duplicate：是否重复
        matched_query：匹配到的搜索词
        similarity：最高相似度
        method：判断方式
        """

        if not query or not query.strip():
            raise ValueError("搜索词不能为空")

        best_match = None
        best_similarity = 0.0
        best_method = None

        normalized_query = self.normalize_query(query)

        for existing_query in existing_queries:
            if not existing_query or not existing_query.strip():
                continue

            # 第一层：标准化字符串去重
            if normalized_query == self.normalize_query(existing_query):
                return {
                    "is_duplicate": True,
                    "matched_query": existing_query,
                    "similarity": 1.0,
                    "method": "exact"
                }

            # 第二层：Embedding 语义去重
            query_embedding = self.get_cached_embedding(query)
            existing_embedding = self.get_cached_embedding(
                existing_query
            )

            similarity = cosine_similarity(
                query_embedding,
                existing_embedding
            )

            if similarity > best_similarity:
                best_similarity = similarity
                best_match = existing_query
                best_method = "embedding"

        return {
            "is_duplicate": best_similarity >= self.threshold,
            "matched_query": best_match,
            "similarity": best_similarity,
            "method": best_method
        }