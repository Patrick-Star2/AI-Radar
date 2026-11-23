
import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

EMBEDDING_API_KEY = os.getenv("EMBEDDING_API_KEY")
EMBEDDING_BASE_URL = os.getenv("EMBEDDING_BASE_URL")
EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "qwen3.7-text-embedding"
)


def get_embedding_client():
    if not EMBEDDING_API_KEY:
        raise ValueError("缺少 EMBEDDING_API_KEY")

    if not EMBEDDING_BASE_URL:
        raise ValueError("缺少 EMBEDDING_BASE_URL")

    return OpenAI(
        api_key=EMBEDDING_API_KEY,
        base_url=EMBEDDING_BASE_URL
    )


def get_embedding(text: str) -> list[float]:
    """
    将一段文本转换为 Embedding 向量。
    """
    client = get_embedding_client()

    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text,
        dimensions=1024
    )

    return response.data[0].embedding