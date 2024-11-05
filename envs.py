import json
import os
from dotenv import load_dotenv

INTERVAL = 300  # seconds
NICS = []


def init():
    global INTERVAL, NICS
    load_dotenv()
    INTERVAL = int(os.getenv("INTERVAL"))
    NICS = json.loads(os.getenv("NICS") or "[]")
