"""
---
title: "Hello World Task"
description: "A simple example task that runs every 5 minutes"
dependencies: []
enabled: true
timeout: 60
---
"""

import time
from datetime import datetime

from helpers import log_info, log_task_complete, log_task_start
from task_scheduler.decorators import every, repeat


@repeat(every(1).minutes)
def start():
    """Simple hello world task that runs every 5 minutes"""
    log_task_start()

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_info(f"Current time: {current_time}")

    print(f"Hello World! Current time: {current_time}")

    # Simulate some work
    time.sleep(2)

    print("Hello World task completed successfully!")
    log_task_complete(duration=2.0)
