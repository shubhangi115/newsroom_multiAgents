from app.llm.client import llm_client
from app.llm.prompts import FACT_CHECK_SYSTEM_PROMPT
from app.schemas import FactCheckReport, ResearchReport


class FactCheckAgent:     #                 |---> chanigng str to ResearchReport , so Now we will remove the temporary JSON string (remember indent=2)
    #                                       |                                         
    async def run(self,research_report: ResearchReport) -> FactCheckReport:

        user_prompt = (
            "Review and fact-check the following newsroom research report.\n\n"
            "RESEARCH REPORT:\n"
            f"{research_report.model_dump_json(indent=2)}" # changing the object to "JSON text", meaning a string that happens to be written in JSON format.
            # as gemini need str not object
        )

        fact_check_report = await llm_client.generate_structured(
            system_prompt=FACT_CHECK_SYSTEM_PROMPT,
            user_prompt=user_prompt,
            response_schema=FactCheckReport
        )

        return fact_check_report


fact_check_agent = FactCheckAgent()