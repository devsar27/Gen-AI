from langchain_community.utilities import GoogleSerperAPIWrapper
from config import SERPER_API_KEY


def get_search_tool():
    """Return a list of search tools for the agent."""
    search = GoogleSerperAPIWrapper(serper_api_key=SERPER_API_KEY)
    return [search.run]


# Future extension: add other ops-specific tools here if needed
