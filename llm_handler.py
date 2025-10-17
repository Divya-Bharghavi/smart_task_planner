from dotenv import load_dotenv
import os

# Load .env from the same folder as this file
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in backend/.env")


def call_llm_generate_plan(goal_text: str):
    # This is a dummy example. Later replace with actual OpenAI API call.
    return [
        {
            "task": "Define objectives",
            "description": "Set clear goals for the project",
            "depends_on": [],
            "estimate_hours": 2,
            "suggested_day": 1
        },
        {
            "task": "Create timeline",
            "description": "Break the project into smaller tasks",
            "depends_on": ["Define objectives"],
            "estimate_hours": 3,
            "suggested_day": 2
        }
    ]
