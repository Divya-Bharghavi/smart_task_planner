from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .schemas import GeneratePlanRequest, GeneratePlanResponse, TaskItem
from .llm_handler import call_llm_generate_plan

app = FastAPI(title="Smart Task Planner API")

# Allow local frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Smart Task Planner API is running"}

@app.post("/generate_plan", response_model=GeneratePlanResponse)
async def generate_plan(req: GeneratePlanRequest):
    try:
        tasks = call_llm_generate_plan(req.goal_text)
        validated_tasks = [
            TaskItem(
                task=t.get("task", "Untitled Task")[:200],
                description=t.get("description", "")[:1000],
                depends_on=t.get("depends_on", []),
                estimate_hours=t.get("estimate_hours", None),
                suggested_day=t.get("suggested_day", None),
            )
            for t in tasks
        ]
        return GeneratePlanResponse(goal_text=req.goal_text, tasks=validated_tasks)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
