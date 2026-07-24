import os

from dotenv import load_dotenv


# Load variables from the .env file into the process environment.
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is missing"
    )

GEMINI_MODEL = os.getenv("GEMINI_MODEL")

if not GEMINI_MODEL:
    raise ValueError(
        "GEMINI_MODEL is missing."
    )

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

if not TAVILY_API_KEY:
    raise ValueError(
        "TAVILY_API_KEY is missing from the environment variables."
    )

LLM_TEMPERATURE = float(
    os.getenv("LLM_TEMPERATURE")
)

LLM_MAX_OUTPUT_TOKENS = int(
    os.getenv("LLM_MAX_OUTPUT_TOKENS")
)



