from fastapi import FastAPI

from app.routes.research import router as research_router


app = FastAPI(
    title="Newsroom AI",
    description="Multi-Agent AI Newsroom Backend",
    version="1.0.0"
)


@app.get("/")
async def health_check():

    return {
        "message": "Newsroom AI Backend is running."
    }


app.include_router(research_router)