from typing import Union
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi import FastAPI, Query
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from fastapi import Form
import json
import joblib
from datetime import datetime
from datetime import date

model = joblib.load("model/task_classifier.pkl")
difficulty_model = joblib.load("model/best_difficulty_model.pkl")


DATA_PATH = Path("data/data.json")


def load_tasks():
    if not DATA_PATH.exists():
        return []

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        tasks = json.load(f)

    # 👇 автоматично додаємо id, якщо його нема
    for index, task in enumerate(tasks, start=1):
        if "id" not in task:
            task["id"] = index

    return tasks

def save_tasks(tasks):
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)






app = FastAPI()
app.mount("/static", StaticFiles(directory="UI/static"), name="static")


class TaskUpdate(BaseModel):
    due_to: str | None = None
    priority: str | None = None
    status: str | None = None
    description: str | None = None


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    with open('UI/templates/index.html', 'rb') as file:
        return HTMLResponse(file.read(), status_code=200)


@app.get("/tasks")
def get_tasks(
    page: int = Query(1, ge=1),
    limit: int = Query(15, ge=1, le=100)
):
    tasks = load_tasks()

    start = (page - 1) * limit
    end = start + limit

    return {
        "items": tasks[start:end],
        "total": len(tasks),
        "page": page,
        "limit": limit
    }
@app.get("/tasks/today")
def get_today_tasks():
    tasks = load_tasks()
    today = date.today().isoformat()
    return [t for t in tasks if t.get("due_to") == today]

@app.get("/tasks/all")
def get_all_tasks():
    return load_tasks()

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            return task
    return {"error": "Task not found"}
@app.put("/tasks/{task_id}")


def update_task(task_id: int, data: TaskUpdate):
    tasks = load_tasks()

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

            task["last_updated"] = "now"  # пізніше зробимо datetime

            save_tasks(tasks)
            return task

    return {"error": "Task not found"}


@app.get("/tasks-page")
def tasks_page():
    
    with open("UI/templates/tasks.html", 'rb') as file:
        return HTMLResponse(file.read(), status_code=200)

@app.post("/add_task")
def add_task(
    title: str = Form(...),
    description: str = Form("")
):
    tasks = load_tasks()

    new_id = max([t.get("id", 0) for t in tasks], default=0) + 1

    text = f"{title} {description}"
    predicted_category = model.predict([text])[0]
    # text = f"{title} {description}"

    difficulty = difficulty_model.predict([text])[0]
    new_task = {
        "id": new_id,
        "title": title,
        "description": description,
        "category": predicted_category,  # 👈 ML тут
        "difficulty" : difficulty,
        "priority": "medium",
        "status": "pending",
        "created_at": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "last_updated": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "history": []
    }

    tasks.append(new_task)
    save_tasks(tasks)

    return {"status": "ok", "category": predicted_category}

@app.post("/classify_all_tasks")
def classify_all_tasks():
    tasks = load_tasks()

    for task in tasks:
        if "category" not in task:
            text = f"{task['title']} {task.get('description', '')}"
            task["category"] = model.predict([text])[0]
        text = f"{task['title']} {task.get('description', '')}"

        task["difficulty"] = difficulty_model.predict([text])[0]

    save_tasks(tasks)
    return {"status": "classified", "count": len(tasks)}


@app.post("/add_project")
def add_project():
    return RedirectResponse("/tasks", status_code=303)


@app.get("/dashboard")
def dashboard_page():
    with open("UI/templates/dashboard.html", "rb") as f:
        return HTMLResponse(f.read(), status_code=200)

@app.get("/dashboard/difficulty")
def dashboard_difficulty():
    return HTMLResponse(
        open("UI/templates/dashboards/dashboard_difficulty.html", "rb").read()
    )

@app.get("/dashboard/models")
def dashboard_models():
    return HTMLResponse(
        open("UI/templates/dashboards/dashboard_models.html", "rb").read()
    )

@app.get("/dashboard/advice")
def dashboard_advice():
    return HTMLResponse(
        open("UI/templates/dashboards/dashboard_advice.html", "rb").read()
    )


@app.get("/api/model-metrics")
def get_model_metrics():
    with open("model/metrics.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return JSONResponse(content=data)





from fastapi import Body

@app.post("/tasks")
def create_task(task: dict = Body(...)):
    tasks = load_tasks()
    task["id"] = max(t["id"] for t in tasks) + 1
    tasks.append(task)
    save_tasks(tasks)
    return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    tasks = load_tasks()
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)
    return {"status": "deleted"}
