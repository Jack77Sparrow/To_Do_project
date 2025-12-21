from typing import Union
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse, FileResponse
from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from fastapi import Form, File, UploadFile
import json
import joblib
from datetime import datetime
from datetime import date
import asyncio
from repository.tasks import load_tasks, save_tasks


model = joblib.load("model/task_classifier.pkl")
difficulty_model = joblib.load("model/best_difficulty_model.pkl")




async def formating_task(title,
    description,
    due_to,
    priority,
    status):
    tasks = await load_tasks()
    print(due_to, date.today().isoformat())
    due_date = datetime.strptime(due_to, "%Y-%m-%d").date()
    if due_date < date.today():
        print("Task can't be in the past")
        raise HTTPException(
            status_code=400,
            detail="Task can't be in the past"
        )
        
    for task in tasks:
        if title == task['title']:
            raise HTTPException(
                status_code=409,
                detail="Task already exists"
            )
   
    new_id = max([t.get("id", 0) for t in tasks], default=0) + 1

    text = f"{title} {description}"
    predicted_category = model.predict([text])[0]

    difficulty = difficulty_model.predict([text])[0]
    new_task = {
        "id": new_id,
        "title": title,
        "description": description,
        "category": predicted_category,
        "difficulty" : difficulty,
        "priority": priority,
        "status": status,
        "created_at": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "last_updated": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "history": [],
        "due_to": due_to
    }
    tasks.append(new_task)
    return tasks



def get_today(tasks: list[dict]) -> list[dict]:
    """
    get todays tasks
    """
    today = date.today().isoformat()
    return [t for t in tasks if t.get("due_to") == today]


app = FastAPI()
app.mount("/static", StaticFiles(directory="UI/static"), name="static")


class TaskUpdate(BaseModel):
    due_to: str | None = None
    priority: str | None = None
    status: str | None = None
    description: str | None = None


class Task(BaseModel):
    id: int
    title: str
    description: str = ""
    category: str
    difficulty: str
    priority: str
    status: str
    due_to: str
    created_at: str
    last_updated: str





# Головна сторінка сайту
@app.get("/")
def read_root():
    return FileResponse("UI/templates/index.html")



@app.get("/new_task")
def add_task():
    """Show page for creating task"""
    return FileResponse("UI/templates/new_task.html")


# show page with all tasks
@app.get("/tasks-page")
def tasks_page():
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
@app.get("/tasks")
async def get_tasks(
    page: int = Query(1, ge=1),
    limit: int = Query(15, ge=1, le=100)
):
    tasks = await load_tasks()

    start = (page - 1) * limit
    end = start + limit

    return {
        "items": tasks[start:end],
        "total": len(tasks),
        "page": page,
        "limit": limit
    }


# to get all today tasks
@app.get("/tasks/today")
async def get_today_tasks():
    tasks = await load_tasks()
    return get_today(tasks)
    


# to get all tasks
@app.get("/tasks/all")
async def get_all_tasks():
    return await load_tasks()


# to get task by id
@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    tasks = await load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            return task
    return {"error": "Task not found"}

# update task and change last_update to "CurrentTime"
@app.put("/tasks/{task_id}")
async def update_task(task_id: int, data: TaskUpdate):
    tasks = await load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            if data.due_to is not None:
                task["due_to"] = data.due_to

            if data.priority is not None:
                task["priority"] = data.priority

            if data.status is not None:
                task["status"] = data.status

            if data.description is not None:
                task["description"] = data.description

            task["last_updated"] = "now"  

            await save_tasks(tasks)
            return task

    return {"error": "Task not found"}




# post request to add task 
@app.post("/add_task")
async def add_task(
    title: str = Form(...),
    description: str = Form(""),
    due_to: str = Form(""),
    priority: str = Form(""),
    status: str = Form(""),
):
    new_tasks = await formating_task(title, description, due_to, priority, status)
    text = f"{title} {description}"
    predicted_category = model.predict([text])[0]
    
    await save_tasks(new_tasks)

    return {"status": "ok", "category": predicted_category}


# classify all tasks using different models
@app.post("/classify_all_tasks")
async def classify_all_tasks():
    tasks = await load_tasks()

    for task in tasks:
        if "category" not in task:
            text = f"{task['title']} {task.get('description', '')}"
            task["category"] = model.predict([text])[0]

        text = f"{task['title']} {task.get('description', '')}"
        task["difficulty"] = difficulty_model.predict([text])[0]

    await save_tasks(tasks)
    return {"status": "classified", "count": len(tasks)}


@app.post("/add_project")
def add_project():
    return RedirectResponse("/tasks", status_code=303)





@app.get("/api/model-metrics")
def get_model_metrics():
    with open("model/metrics.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return JSONResponse(content=data)


from fastapi import Body

@app.post("/tasks")
async def create_task(task: dict = Body(...)):
    tasks = await load_tasks()
    task["id"] = max(t["id"] for t in tasks) + 1
    tasks.append(task)
    await save_tasks(tasks)
    return task

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    tasks = await load_tasks()
    tasks = [t for t in tasks if t["id"] != task_id]
    await save_tasks(tasks)
    return {"status": "deleted"}


