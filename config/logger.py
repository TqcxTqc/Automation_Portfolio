import logging
from datetime import datetime
from pathlib import Path

LOG_DIR = Path(__file__).resolve().parent.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / f"{datetime.now()}.log"


def setup_logger(name):
    logging.basicConfig(level=logging.INFO, filename=LOG_FILE,
                        format="%(asctime)s: %(levelname)s: %(name)s: %(message)s",
                        datefmt="%m/%d/%Y %I:%M:%S %p")

    return logging.getLogger(name)
