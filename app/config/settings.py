import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    LLM_API_KEY = os.getenv("LLM_API_KEY")
    LLM_BASE_URL = os.getenv("LLM_BASE_URL")
    LLM_MODEL = os.getenv("LLM_MODEL", "qwen4-max")

    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

    @classmethod
    def validate(cls):

        required = {
            "LLM_API_KEY": cls.LLM_API_KEY,
            "LLM_BASE_URL": cls.LLM_BASE_URL,
            "LLM_MODEL": cls.LLM_MODEL,
            "TAVILY_API_KEY": cls.TAVILY_API_KEY
        }

        missing = [
            key for key, value in required.items()
            if not value
        ]

        if missing:
            raise ValueError(
                f"缺少环境变量：{', '.join(missing)}"
            )


settings = Settings()