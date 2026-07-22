from app.llm.client import llm_client
from app.llm.prompts import SEO_SYSTEM_PROMPT
from app.schemas import SEOReport, FactCheckReport


class SEOAgent:

    async def run(self,fact_check_report: FactCheckReport) -> SEOReport:

        user_prompt = (
            "Create an SEO package from the following "
            "fact-checked newsroom report:\n\n"
            f"{fact_check_report.model_dump_json(indent=2)}" # giving gemini str , palin text
        )

        seo_report = await llm_client.generate_structured(
            system_prompt=SEO_SYSTEM_PROMPT,
            user_prompt=user_prompt,
            response_schema=SEOReport
        )

        return seo_report


seo_agent = SEOAgent()