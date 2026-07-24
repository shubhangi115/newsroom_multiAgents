from tavily import AsyncTavilyClient

from app.config import TAVILY_API_KEY


class WebSearchTool:

    def __init__(self):
        self.client = AsyncTavilyClient(
            api_key=TAVILY_API_KEY
        )

    async def search(self, query: str):

        response = await self.client.search(
            query=query,
            search_depth="advanced",
            max_results=5
        )

        return response["results"]


web_search_tool = WebSearchTool()
