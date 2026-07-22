from app.llm.client import llm_client
from app.llm.prompts import QUALITY_VALIDATOR_SYSTEM_PROMPT
from app.schemas import ValidationReport, ResearchReport,FactCheckReport,SEOReport,ScriptReport,ImagePromptReport,VideoPromptReport,HeadlineReport,SocialMediaReport


class QualityValidatorAgent:

    async def run(
        self,
        research_report: ResearchReport,
        fact_check_report: FactCheckReport,
        seo_report: SEOReport,
        script: ScriptReport,
        image_prompt: ImagePromptReport,
        video_prompt: VideoPromptReport,
        headline_report: HeadlineReport,
        social_media_report: SocialMediaReport
    ) -> ValidationReport:

        user_prompt = (
            "Review the complete newsroom package below.\n\n"
            "RESEARCH REPORT:\n"
            f"{research_report.model_dump_json(indent=2)}\n\n"

            "FACT-CHECK REPORT:\n"
            f"{fact_check_report.model_dump_json(indent=2)}\n\n"

            "SEO PACKAGE:\n"
            f"{seo_report.model_dump_json(indent=2)}\n\n"

            "FINAL NEWS ARTICLE:\n"
            f"{script.model_dump_json(indent=2)}\n\n"

            "IMAGE PROMPT:\n"
            f"{image_prompt.model_dump_json(indent=2)}\n\n"

            "VIDEO PROMPT:\n"
            f"{video_prompt.model_dump_json(indent=2)}\n\n"

            "HEADLINE REPORT:\n"
            f"{headline_report.model_dump_json(indent=2)}\n\n"

            "SOCIAL MEDIA REPORT:\n"
            f"{social_media_report.model_dump_json(indent=2)}"
        )

        validation_report = await llm_client.generate_structured(
            system_prompt=QUALITY_VALIDATOR_SYSTEM_PROMPT,
            user_prompt=user_prompt,
            response_schema=ValidationReport
        )

        return validation_report


quality_validator_agent = QualityValidatorAgent()