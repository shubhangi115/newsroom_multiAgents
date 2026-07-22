from app.llm.client import llm_client
from app.llm.prompts import SCRIPT_WRITER_SYSTEM_PROMPT
from app.schemas import ScriptReport,FactCheckReport,ResearchReport,SEOReport


class ScriptWriterAgent:

    async def run(self,research_report: ResearchReport,fact_check_report: FactCheckReport,seo_report: SEOReport) -> ScriptReport:

        user_prompt = (
            "Write a publication-ready news article using the material below.\n\n"
            "RESEARCH REPORT:\n"
            f"{research_report.model_dump_json(indent=2)}\n\n"

            "FACT-CHECK REPORT:\n"
            f"{fact_check_report.model_dump_json(indent=2)}\n\n"

            "SEO PACKAGE:\n"
            f"{seo_report.model_dump_json(indent=2)}"
        )

        article = await llm_client.generate_structured(
            system_prompt=SCRIPT_WRITER_SYSTEM_PROMPT,
            user_prompt=user_prompt,
            response_schema=ScriptReport
        )

        return article


script_writer_agent = ScriptWriterAgent()