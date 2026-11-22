from tavily import TavilyClient
from app.config.settings import settings


def search_web(query: str) -> dict:
    """
    搜索互联网，返回相关信息。
    """

    if not settings.TAVILY_API_KEY:
        return {
            "error": "TAVILY_API_KEY 未配置"
        }

    #创建Tavily客户端
    client = TavilyClient(
        api_key=settings.TAVILY_API_KEY
    )

    try:
        response = client.search(
            query=query,
            max_results=5
        )

        return {
            "query": query,
            "results": response.get("results", [])
        }

    except Exception as e:
        return {
            "error": str(e)
        }