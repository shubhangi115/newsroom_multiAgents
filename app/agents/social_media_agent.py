from app.llm.client import llm_client
from app.llm.prompts import SOCIAL_MEDIA_SYSTEM_PROMPT
from app.schemas import SocialMediaReport,FactCheckReport, ScriptReport,HeadlineReport


class SocialMedia:

    async def run(self,fact_check_report: FactCheckReport,script: ScriptReport, headline_report: HeadlineReport) -> SocialMediaReport:
        user_prompt = (
            f"Create platform-specific social media content using the material below:\n\n"
            "FACT-CHECK REPORT:\n"
            f"{fact_check_report.model_dump_json(indent=2)}\n\n"

            "FINAL SCRIPT:\n"
            f"{script.model_dump_json(indent=2)}\n\n"

            "HEADLINE REPORT:\n"
            f"{headline_report.model_dump_json(indent=2)}"
        )

        media_report = await llm_client.generate_structured(
            system_prompt=SOCIAL_MEDIA_SYSTEM_PROMPT,
            user_prompt=user_prompt,
            response_schema=SocialMediaReport
        )

        return media_report


social_media_agent = SocialMedia()