import asyncio
import aiohttp
from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import Command
from dotenv import load_dotenv
import os
from datetime import date


load_dotenv()
router = Router()

BOT_TOKEN = os.getenv("TOKEN")
API_URL = "http://127.0.0.1:8000"

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(msg: types.Message):
    await msg.answer(
        "👋 Intelligent Task Manager\n\n"
        "/today – Today's tasks\n"
        "/add – Add new task"
    )


@dp.message(Command("today"))
async def today_tasks(msg: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{API_URL}/tasks/today") as resp:
            tasks = await resp.json()
            print(tasks)

    if not tasks:
        await msg.answer("🎉 No tasks for today!")
        return

    text = "Today's tasks:\n\n"
    for t in tasks:
        text += f"• {t['title']} ({t.get('difficulty', '-')})\n"

    await msg.answer(text)



@dp.message(Command("add"))
async def add_task_command(message):
    text = message.text.replace("/add", "").strip()

    if not text:
        await message.answer("❗ Usage:\n/add Task title | description")
        return

    if "|" in text:
        title, description = map(str.strip, text.split("|", 1))
    else:
        title = text
        description = ""

    payload = {
        "title": title,
        "description": description
    }
    API_URL = "http://127.0.0.1:8000/add_task"
    async with aiohttp.ClientSession() as session:
        async with session.post(API_URL, data=payload) as resp:
            result = await resp.json()

    await message.answer(
    "✅ Task added successfully!\n\n"
    f"📌 Title: {title}\n"
    f"🧠 Category: {result.get('category', '-')}\n"
    f"⚡ Difficulty: {result.get('difficulty', '-')}"
)

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
