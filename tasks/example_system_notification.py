"""
---
title: "System Notification Task"
description: "Sends periodic system notifications to the user's operating system"
dependencies: []
enabled: true
timeout: 60
---
"""

from datetime import datetime

from helpers import log_error, log_execution_result, log_info, log_task_complete, log_task_start
from helpers.system_notifications import send_and_log_notification
from task_scheduler.decorators import every, repeat


@repeat(every(5).minutes)
def start():
    """Send a hello world notification every 5 minutes"""
    try:
        log_task_start()
        log_info("Preparing system notification...")

        # Get current time for personalized message
        current_time = datetime.now().strftime("%H:%M:%S")
        current_date = datetime.now().strftime("%Y-%m-%d")

        # Prepare notification content
        title = "Task Scheduler Hello"
        message = f"Hello World! 🌍\nTime: {current_time}\nDate: {current_date}"

        # Send the notification using helper function
        log_info(f"Sending notification: '{title}'")
        print(f"Sending notification: '{title}'")

        result = send_and_log_notification(
            title=title, message=message, timeout=8, urgency="normal", app_name="Task Scheduler"
        )

        # Log the execution result
        log_execution_result(
            operation="send_notification",
            success=result["success"],
            details={
                "method": result.get("method"),
                "log_file": result.get("log_file"),
                "title": title,
            },
        )

        # Log the result
        if result["success"]:
            log_info(f"Notification sent successfully using {result['method']}")
            print(f"✅ Notification sent successfully using {result['method']}")
            print(f"Notification logged to: {result['log_file']}")
        else:
            log_error(f"Notification failed: {result['error']}")
            print(f"❌ Notification failed: {result['error']}")

        # Print summary
        print("System notification task completed successfully!")
        log_task_complete()

    except Exception as e:
        log_error(f"Error in notification task: {e}", exception=e)
        print(f"Error in notification task: {e}")
        raise
