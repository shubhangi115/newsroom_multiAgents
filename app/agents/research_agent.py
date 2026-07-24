from app.llm.client import llm_client
from app.llm.prompts import RESEARCH_SYSTEM_PROMPT
from app.schemas import ResearchReport,ResearchSource
from app.tool.web_search import web_search_tool


class ResearchAgent:

    # async def run(self, topic: str) -> str:
    async def run(self, topic: str) ->  ResearchReport: # changing return type from str to the ResearchReport(the json schema)
        
        # tavily 
        # searching the topic 
        try:
            search_results = await web_search_tool.search(topic)
        
        except Exception as error:
            print(f"Tavily search failed: {error}")
            search_results = []

        # results into readable text
        formatted_results = ""

        for index in range(len(search_results)):

            result = search_results[index]

            title = result.get("title", "No title")
            url = result.get("url", "No URL")
            content = result.get("content", "No content")

            formatted_results += (
                f"\nSource {index + 1}:\n"
                f"Title: {title}\n"
                f"URL: {url}\n"
                f"Content: {content}\n"
            )

        # giving both the topic and live results to Gemini
        if len(search_results) >0: # there is no tavily error so use tavily api or it returned search results so use it 
            user_prompt = (
                f"Research the following newsroom topic using the live web search results as the primary source of information   :\n\n"
                f"Topic: {topic}\n\n"
                f"Live Web Search Results:\n"
                f"{formatted_results}"
            )
        
        else: # when the tavily error occurs use the gemini knowledge 

            user_prompt = (
                f"Research the following newsroom topic.\n\n"
                f"Topic: {topic}\n\n"
                f"Live web search results are currently unavailable. "
                f"Use your existing knowledge, avoid presenting uncertain "
                f"information as confirmed, and clearly mention claims that "
                f"require verification."
            )

        # user_prompt = (
        #     f"Research the following newsroom topic:\n\n"
        #     f"{topic}"
        # )

        research_report = await llm_client.generate_structured(
            system_prompt=RESEARCH_SYSTEM_PROMPT,
            user_prompt=user_prompt,
            response_schema=ResearchReport # adding for the json structured output
        )

        # creating sources field in the ouput
        sources = []

        for index in range(len(search_results)):

            result = search_results[index]

            source = ResearchSource(
                title=result.get("title", "No title"),
                url=result.get("url", "No URL")
            )

            sources.append(source)

        research_report.sources = sources

        return research_report

        # now the it is returning obejct we will :
        # Now update ResearchResponse so the research field accepts a structured ResearchReport object instead of a string.


research_agent = ResearchAgent()