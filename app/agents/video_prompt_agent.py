from app.llm.client import llm_client
from app.llm.prompts import VIDEO_PROMPT_SYSTEM_PROMPT
from app.schemas import VideoPromptReport,ImagePromptReport,FactCheckReport,ScriptReport


class VideoPromptAgent:

    async def run(
        self,
        fact_check_report: FactCheckReport,
        script: ScriptReport,
        image_prompt: ImagePromptReport,
    ) -> VideoPromptReport:

        user_prompt = (
            "Create a professional newsroom video prompt and scene plan "
            "using the material below.\n\n"
            "FACT-CHECK REPORT:\n"
            f"{fact_check_report.model_dump_json(indent=2)}\n\n"

            "FINAL NEWS ARTICLE:\n"
            f"{script.model_dump_json(indent=2)}\n\n"

            "IMAGE PROMPT:\n"
            f"{image_prompt.model_dump_json(indent=2)}"
        )

        video_prompt = await llm_client.generate_structured(
            system_prompt=VIDEO_PROMPT_SYSTEM_PROMPT,
            user_prompt=user_prompt,
            response_schema=VideoPromptReport
        )

        return video_prompt


video_prompt_agent = VideoPromptAgent()