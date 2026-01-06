import os

from dotenv import load_dotenv
from openai import AsyncAzureOpenAI, AsyncOpenAI

from agents import OpenAIChatCompletionsModel

load_dotenv(override=True)

openai_api_key = os.getenv("OPENAI_API_KEY")
google_api_key = os.getenv("GOOGLE_API_KEY")
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")
azure_api_key = os.getenv("AZURE_API_KEY")
perplexity_api_key = os.getenv("PERPLEXITY_API_KEY")

GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
DEEPSEEK_BASE_URL = "https://api.deepseek.com/v1"
GROQ_BASE_URL = "https://api.groq.com/openai/v1"
PERPLEXITY_BASE_URL = "https://api.perplexity.ai"
AZURE_BASE_URL = os.getenv("AZURE_ENDPOINT")


deepseek_client = AsyncOpenAI(base_url=DEEPSEEK_BASE_URL, api_key=deepseek_api_key)
gemini_client = AsyncOpenAI(base_url=GEMINI_BASE_URL, api_key=google_api_key)
groq_client = AsyncOpenAI(base_url=GROQ_BASE_URL, api_key=groq_api_key)
perplexity_client = AsyncOpenAI(
    base_url=PERPLEXITY_BASE_URL, api_key=perplexity_api_key
)
azure_client = AsyncAzureOpenAI(
    azure_endpoint=AZURE_BASE_URL,
    api_key=azure_api_key,
    api_version="2025-01-01-preview",
)

deepseek_model = OpenAIChatCompletionsModel(
    model="deepseek-chat", openai_client=deepseek_client
)
gemini_model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash", openai_client=gemini_client
)
llama3_3_model = OpenAIChatCompletionsModel(
    model="llama-3.3-70b-versatile", openai_client=groq_client
)
perplexity_model = OpenAIChatCompletionsModel(
    model="sonar-pro", openai_client=perplexity_client
)
azure_model = OpenAIChatCompletionsModel(model="gpt-5", openai_client=azure_client)
