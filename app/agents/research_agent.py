from app.llm.client import llm_client
from app.llm.prompts import RESEARCH_SYSTEM_PROMPT
from app.schemas import ResearchReport


class ResearchAgent:

    # async def run(self, topic: str) -> str:
    async def run(self, topic: str) ->  ResearchReport: # changing return type from str to the ResearchReport(the json schema)
        user_prompt = (
            f"Research the following newsroom topic:\n\n"
            f"{topic}"
        )

        research_report = await llm_client.generate_structured(
            system_prompt=RESEARCH_SYSTEM_PROMPT,
            user_prompt=user_prompt,
            response_schema=ResearchReport # adding for the json structured output
        )

        return research_report

        # now the it is returning obejct we will :
        # Now update ResearchResponse so the research field accepts a structured ResearchReport object instead of a string.


research_agent = ResearchAgent()