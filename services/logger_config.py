import logging
from pathlib import Path

# Absolute path for the log file
ROOT_DIR = Path(__file__).resolve().parents[1]  # adjust to your project root

LOG_FILE = ROOT_DIR / "logs" / "daily_task.log"
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

# Create a logger
logger = logging.getLogger("my_project")
logger.setLevel(logging.INFO)

# File handler
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add handler to logger
logger.addHandler(file_handler)
