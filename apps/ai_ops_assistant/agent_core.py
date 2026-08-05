from langchain_groq import ChatGroq
from langchain.agents import create_agent
from prompts import SYSTEM_PROMPT
from tools import get_search_tool
from config import GROQ_API_KEY


def build_agent():
    model = ChatGroq(model="openai/gpt-oss-20b", api_key=GROQ_API_KEY)
    tools = get_search_tool()

    agent = create_agent(
        model=model,
        tools=tools,
        system_prompt=SYSTEM_PROMPT,
    )
    return agent
