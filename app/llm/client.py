from google import genai
from google.genai import errors,types
import asyncio

# for the structured JSON format to return ,instead of single string 
from pydantic import BaseModel

from app.config import (
    GEMINI_API_KEY,
    GEMINI_MODEL,
    LLM_TEMPERATURE,
    LLM_MAX_OUTPUT_TOKENS
)

# creating a class to handle the LLM client and its methods
# it will do :create the provider client,send prompts,apply common model settings,extract the generated responseclass LLMClient:
class LLMClient:

    # constructor to initialize the LLM client with the provided API key, model, temperature, and max output tokens
    def __init__(self):

        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

        self.model = GEMINI_MODEL

        self.temperature = LLM_TEMPERATURE

        self.max_output_tokens = LLM_MAX_OUTPUT_TOKENS
    
    # method to generate content from the LLM model using the provided system and user prompts which is asynchronus meaning it can be awaited and will not block the execution of other code while waiting for the response
    async def generate(self,system_prompt: str,user_prompt: str) -> str:

        max_attempts = 3

        for attempt in range(max_attempts):
            try:
                response = await self.client.aio.models.generate_content(
                    model=self.model,
                    contents=user_prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=system_prompt,
                        temperature=self.temperature,
                        max_output_tokens=self.max_output_tokens,
                    ),
                )

                if response.text is None:
                    raise ValueError(
                        "Gemini returned an empty text response."
                    )

                return response.text

            except errors.APIError as error:
                retryable_codes = [429, 500, 502, 503, 504]

                is_retryable = error.code in retryable_codes
                is_last_attempt = attempt == max_attempts - 1

                if not is_retryable or is_last_attempt:
                    raise

                wait_seconds = 2 ** attempt

                print(
                    f"Gemini temporarily failed with {error.code}. "
                    f"Retrying in {wait_seconds} second(s)..."
                )

                await asyncio.sleep(wait_seconds)

        raise RuntimeError(
            "Gemini request failed after all retry attempts."
        )
    
    # for the structured JSON format to return ,instead of single string 
    async def generate_structured(
        self,
        system_prompt: str,
        user_prompt: str,
        response_schema: type[BaseModel]
    ) -> BaseModel:

        max_attempts = 3

        for attempt in range(max_attempts):

            try:

                response = await self.client.aio.models.generate_content(
                    model=self.model,
                    contents=user_prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=system_prompt,
                        temperature=self.temperature,
                        max_output_tokens=self.max_output_tokens,
                        response_mime_type="application/json",
                        response_schema=response_schema
                    )
                )

                if response.parsed is None:
                    # to debugg
                    # print("\n========== RAW RESPONSE ==========")
                    # print("TEXT:")
                    # print(response.text)
                    # print()

                    # print("PARSED:")
                    # print(response.parsed)
                    # print()

                    # print("FULL RESPONSE:")
                    # print(response)
                    # print("=================================\n")

                    raise ValueError(
                        "Gemini returned an empty structured response."
                    )

                return response.parsed


            except errors.APIError as error:

                retryable_codes = [429, 500, 502, 503, 504]

                is_retryable = error.code in retryable_codes
                is_last_attempt = attempt == max_attempts - 1

                if not is_retryable or is_last_attempt:
                    raise


                wait_seconds = 2 ** attempt

                print(
                    f"Gemini temporarily failed with {error.code}. "
                    f"Retrying in {wait_seconds} second(s)..."
                )

                await asyncio.sleep(wait_seconds)


        raise RuntimeError(
            "Gemini structured request failed after all retry attempts."
        )

llm_client = LLMClient()