# AI Newsroom Multi-Agent System

An AI-powered newsroom application that automates news generation using multiple AI agents.

## Live Demo
> https://newsroom-ai-multiagent.streamlit.app

## Features

- News Research
- Fact Checking
- SEO Optimization
- Script Generation
- Image Prompt Generation
- Video Prompt Generation
- Headline Generation
- Social Media Content Generation
- Quality Validation
- Final Editorial Review

## Tech Stack

- Python
- FastAPI
- Streamlit
- Google Gemini API
- Tavily API

## Run Locally
### Clone the repository

```bash
git clone https://github.com/shubhangi115/newsroom_multiagent.git
cd newsroom_multiagent
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start Backend

```bash
uvicorn app.main:app --reload
```

### Start Frontend

```bash
streamlit run frontend/home.py
```

## Environment Variables

Create a `.env` file and add:

```env
GEMINI_API_KEY=your_api_key
TAVILY_API_KEY=your_api_key
GEMINI_MODEL=gemini-2.5-flash
LLM_TEMPERATURE=0.2
LLM_MAX_OUTPUT_TOKENS=1500
```


