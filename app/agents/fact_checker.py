from app.llm.client import llm_client
from app.llm.prompts import FACT_CHECK_SYSTEM_PROMPT
from app.schemas import FactCheckReport, ResearchReport
from app.tool.web_search import web_search_tool


class FactCheckAgent:     #                 |---> chanigng str to ResearchReport , so Now we will remove the temporary JSON string (remember indent=2)
    #                                       |                                         
    async def run(self,research_report: ResearchReport) -> FactCheckReport:
        verification_results=""
        
        for index in range(
            len(research_report.claims_requiring_verification)
        ):

            claim = (
                research_report
                .claims_requiring_verification[index]
            )

            try:
                search_results = await web_search_tool.search(claim)

            except Exception as error:
                print(
                    f"Tavily verification search failed "
                    f"for claim '{claim}': {error}"
                )

                search_results = []

            verification_results += (
                f"\nClaim {index + 1}:\n"
                f"{claim}\n"
            )

            for result_index in range(len(search_results)):

                result = search_results[result_index]

                title = result.get("title", "No title")
                url = result.get("url", "No URL")
                content = result.get("content", "No content")

                verification_results += (
                    f"\nEvidence {result_index + 1}:\n"
                    f"Title: {title}\n"
                    f"URL: {url}\n"
                    f"Content: {content}\n"
                )

        user_prompt = (
            "Review and fact-check the following newsroom research report.\n\n"
            "Use the verification search evidence to evaluate the claims. Do not assume that a claim is correct only because it appears in the research report.\n\n"
            "RESEARCH REPORT:\n"
            f"{research_report.model_dump_json(indent=2)}" # changing the object to "JSON text", meaning a string that happens to be written in JSON format.
            # as gemini need str not object

            # verification from the tavily 
            "VERIFICATION SEARCH EVIDENCE:\n"
            f"{verification_results}"
        )

        fact_check_report = await llm_client.generate_structured(
            system_prompt=FACT_CHECK_SYSTEM_PROMPT,
            user_prompt=user_prompt,
            response_schema=FactCheckReport
        )

        return fact_check_report


fact_check_agent = FactCheckAgent()