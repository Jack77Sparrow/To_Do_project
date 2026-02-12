import logging
from pathlib import Path

# Absolute path for the log file
ROOT_DIR = Path(__file__).resolve().parents[1]  # adjust to your project root

LOG_FILE = ROOT_DIR / "logs" / "daily_task.log"
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

# setting logger
logging.basicConfig(
    level=logging.INFO,  # мінімальний рівень, що буде записуватись
    format="%(asctime)s - %(levelname)s - %(module)s.%(funcName)s: %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()  # також в консоль
    ]
)

logger = logging.getLogger("my_project")
