from app.llm.client import llm_client
from app.llm.prompts import FINAL_EDITOR_SYSTEM_PROMPT
from app.schemas import FinalReport, ValidationReport,FactCheckReport,SEOReport,ScriptReport,ImagePromptReport,VideoPromptReport,HeadlineReport,SocialMediaReport

class FinalEditorAgent:

    async def run(
        self,
        fact_check_report: FactCheckReport,
        seo_report: SEOReport,
        script: ScriptReport,
        headline_report: HeadlineReport,
        social_media_report: SocialMediaReport,
        validation_report: ValidationReport
    ) -> FinalReport:

        user_prompt = (
            "Prepare the final publication-ready newsroom package "
            "using the material below.\n\n"

            "FACT-CHECK REPORT:\n"
            f"{fact_check_report.model_dump_json(indent=2)}\n\n"

            "SEO PACKAGE:\n"
            f"{seo_report.model_dump_json(indent=2)}\n\n"

            "FINAL NEWS ARTICLE DRAFT:\n"
            f"{script.model_dump_json(indent=2)}\n\n"

            "HEADLINE REPORT:\n"
            f"{headline_report.model_dump_json(indent=2)}\n\n"

            "SOCIAL MEDIA REPORT:\n"
            f"{social_media_report.model_dump_json(indent=2)}\n\n"

            "QUALITY VALIDATION REPORT:\n"
            f"{validation_report.model_dump_json(indent=2)}"
        )

        final_package = await llm_client.generate_structured(
            system_prompt=FINAL_EDITOR_SYSTEM_PROMPT,
            user_prompt=user_prompt,
            response_schema=FinalReport
        )

        return final_package


final_editor_agent = FinalEditorAgent()