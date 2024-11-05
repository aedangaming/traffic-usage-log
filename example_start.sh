#!/usr/bin/bash

# change the path below
cd /path/to/traffic-usage-log && \
python3 -m venv .venv && \
source .venv/bin/activate && \
pip install -r requirements.txt && \
python3 main.py
