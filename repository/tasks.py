import aiofiles
import json
import asyncio
from pathlib import Path





DATA_PATH = Path("data/data.json")

async def load_tasks():
    """функція для завантаження даних з задачами"""
    try:
        async with aiofiles.open(DATA_PATH, "r", encoding="utf-8") as f:
            data = await f.read()
    except FileNotFoundError:
        return []
    
    tasks = json.loads(data)

    # автоматично додаємо id, якщо його нема
    for index, task in enumerate(tasks, start=1):
        if "id" not in task:
            task["id"] = index

    return tasks

lock = asyncio.Lock()
async def save_tasks(tasks):
    """функція для збереження задач в json файл"""
    json_string = json.dumps(tasks, ensure_ascii=False, indent=4)

    tmp_path = DATA_PATH.with_suffix(".tmp")
    async with lock:
        async with aiofiles.open(tmp_path, "w", encoding="utf-8") as f:
            await f.write(json_string)

        tmp_path.replace(DATA_PATH)