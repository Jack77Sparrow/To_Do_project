
from fastapi.responses import RedirectResponse, JSONResponse, FileResponse
from fastapi import FastAPI, Query
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi import Form
from fastapi.exceptions import HTTPException
import json
from datetime import datetime, date
from typing import Optional, List, Dict

from services.tasks import (get_all_tasks_service, 
                            get_today_tasks_service, 
                            get_task_by_id, 
                            update_task_service, 
                            add_task_to_database, 
                            delete_task_from_db, 
                            add_task_timer_services, 
                            update_task_timer_services,
                            select_active_tasks_services)


app = FastAPI()
app.mount("/static", StaticFiles(directory="UI/static"), name="static")





# -- task update model
class TaskUpdate(BaseModel):
    due_to: Optional[str] = None
    priority: Optional[str] = None
    status: Optional[str] = None
    description: Optional[str] = None

# -- task model 
class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = ""
    category: str
    difficulty: str
    priority: Optional[str] = None
    status: str
    created_at: datetime
    last_updated: Optional[datetime] = None
    due_to: Optional[date] = None


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    status: str
    priority: str
    difficulty: str
    category: str
    created_at: datetime
    last_updated: datetime
    due_to: date | None

    class Config:
        from_attributes = True  


@app.get("/")
def read_root():
    """Main page"""
    return FileResponse("UI/templates/index.html")


@app.get("/new_task")
def add_task():
    """Creating task page"""
    return FileResponse("UI/templates/new_task.html")


@app.get("/tasks-page")
def tasks_page():
    """Page with all tasks"""
    return FileResponse("UI/templates/tasks.html")


@app.get("/dashboard")
def dashboard_page():
    """Shows dashboard page"""
    return FileResponse("UI/templates/dashboard.html")



# DASHBOARD PAGES
@app.get("/dashboard/difficulty")
def dashboard_difficulty():
    """Dashboard difficulty page"""
    return FileResponse("UI/templates/dashboards/dashboard_difficulty.html")

@app.get("/dashboard/models")
def dashboard_models():
    """Dashboard models-info page"""
    return FileResponse("UI/templates/dashboards/dashboard_models.html")

@app.get("/dashboard/advice")
def dashboard_advice():
    """Dashboard advice page"""
    return FileResponse("UI/templates/dashboards/dashboard_advice.html")





# Сторінка з усіма тасками
@app.get("/tasks", response_model=List[TaskResponse])
async def get_tasks(
    page: int = Query(1, ge=1),
    limit: int = Query(15, ge=1, le=100),
    status: str | None = Query(None),
    priority: str | None = Query(None),
    difficulty: str | None = Query(None)
):
    # tasks = await load_tasks()
    
    tasks = get_all_tasks_service(status=status, 
                                  priority=priority, 
                                  difficulty=difficulty)

    offset = (page-1)*limit
    end = offset + limit


    return {
        "items": tasks[offset:end],
        "total": len(tasks),
        "page": page,
        "limit": limit
    }


# to get all today tasks
@app.get("/tasks/today")
async def get_today_tasks():
    return get_today_tasks_service
    


# to get all tasks
@app.get("/tasks/all")
async def get_all_tasks():
    return get_all_tasks_service()


# to get task by id
@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    task = get_task_by_id(task_id=task_id)
    return Task(**task)


# update task and change last_update to "CurrentTime"
@app.patch("/tasks/{task_id}")
async def update_task(task_id: int, data: TaskUpdate):
        # tasks = await load_tasks()
    
    updated = update_task_service(task_id=task_id, update_data=data)
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return {'status': "updated"}






# post request to add task 
@app.post("/add_task")
async def add_task(
    title: str = Form(...),
    description: str = Form(""),
    due_to: str = Form(""),
    priority: str = Form(""),
    status: str = Form(""),
):

    return add_task_to_database({'title': title, 
                                 'description':description,  
                                 'due_to':due_to, 
                                 'priority': priority, 
                                 'status': status})



@app.post("/add_project")
def add_project():
    return RedirectResponse("/tasks", status_code=303)


@app.post("/tasks/{task_id}/start")
def start_task_timer(task_id: int):
    return add_task_timer_services(task_id=task_id)


@app.post("/tasks/{task_id}/stop")
def stop_task_timer(task_id: int):
    return update_task_timer_services(task_id=task_id)



@app.get("/timer/active")
def timer_active():
    data = select_active_tasks_services()
    return {"timer data": data}



@app.get("/api/model-metrics")
def get_model_metrics():
    with open("model/metrics.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return JSONResponse(content=data)



@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    """delete task by id"""
    return delete_task_from_db(task_id=task_id)


