from app.llm.client import llm_client
from app.llm.prompts import IMAGE_PROMPT_SYSTEM_PROMPT
from app.schemas import ImagePromptReport,FactCheckReport,ScriptReport,ResearchReport


class ImagePromptAgent:

    async def run(self,fact_check_report: FactCheckReport,script: ScriptReport,) -> ImagePromptReport:

        user_prompt = (
            "Create an editorial image prompt using the material below.\n\n"

            "FACT-CHECK REPORT:\n"
            f"{fact_check_report.model_dump_json(indent=2)}\n\n"

            "FINAL NEWS ARTICLE:\n"
            f"{script.model_dump_json(indent=2)}"
        )

        image_prompt = await llm_client.generate_structured(
            system_prompt=IMAGE_PROMPT_SYSTEM_PROMPT,
            user_prompt=user_prompt,
            response_schema=ImagePromptReport
        )

        return image_prompt


image_prompt_agent = ImagePromptAgent()