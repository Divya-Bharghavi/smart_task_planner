from pydantic import BaseModel
from typing import List, Optional

class TaskItem(BaseModel):
    task: str
    description: Optional[str] = ""
    depends_on: List[str] = []
    estimate_hours: Optional[int] = None
    suggested_day: Optional[int] = None

class GeneratePlanRequest(BaseModel):
    goal_text: str

class GeneratePlanResponse(BaseModel):
    goal_text: str
    tasks: List[TaskItem]
