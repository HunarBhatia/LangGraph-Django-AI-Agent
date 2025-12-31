from django.conf import settings
from langchain_openai import ChatOpenAI


def get_openai_model(model="gpt-4o"):
    return ChatOpenAI(
        model="gpt-4o",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        api_key=settings.OPENAI_API_KEY,
    )