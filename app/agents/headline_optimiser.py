from app.llm.client import llm_client
from app.llm.prompts import HEADLINE_OPTIMIZER_SYSTEM_PROMPT
from app.schemas import HeadlineReport,FactCheckReport,SEOReport,ScriptReport

class HeadlineOptimiser:

    async def run(self,fact_check_report: FactCheckReport,seo_report: SEOReport,script: ScriptReport) -> str:
        user_prompt = (
            f"Create multiple professional headlines using:\n\n"
            "FACT-CHECK REPORT:\n"
            f"{fact_check_report.model_dump_json(indent=2)}\n\n"

            "SEO PACKAGE:\n"
            f"{seo_report.model_dump_json(indent=2)}\n\n"

            "FINAL NEWS ARTICLE:\n"
            f"{script.model_dump_json(indent=2)}"
        )

        headline_report = await llm_client.generate_structured(
            system_prompt=HEADLINE_OPTIMIZER_SYSTEM_PROMPT,
            user_prompt=user_prompt,
            response_schema=HeadlineReport
        )

        return headline_report


headline_optimiser_agent = HeadlineOptimiser()