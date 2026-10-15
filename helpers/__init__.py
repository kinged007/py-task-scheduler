"""
Task Scheduler Helper Modules

This package contains reusable helper functions for common task operations.
Each helper module has its own dependencies specified in YAML frontmatter.
"""

# Import commonly used functions for easy access
from .config_loader import (
    get_config_value,
    get_project_root,
    list_config_files,
    load_config,
    save_config,
)
from .external_execution import (
    execute_cli_command,
    execute_python_script,
    execute_script_with_retry,
    process_execution_results,
)
from .system_notifications import log_notification, send_and_log_notification, send_notification
from .task_logging import (
    create_task_logger,
    log,
    log_critical,
    log_debug,
    log_error,
    log_execution_result,
    log_info,
    log_structured_data,
    log_task_complete,
    log_task_error,
    log_task_start,
    log_warning,
    task_error,
    task_info,
    task_log,
)

__all__ = [
    # System notifications
    "send_notification",
    "send_and_log_notification",
    "log_notification",
    # External execution
    "execute_python_script",
    "execute_cli_command",
    "process_execution_results",
    "execute_script_with_retry",
    # Task logging
    "log",
    "log_info",
    "log_error",
    "log_warning",
    "log_debug",
    "log_critical",
    "log_task_start",
    "log_task_complete",
    "log_task_error",
    "log_execution_result",
    "log_structured_data",
    "create_task_logger",
    "task_log",
    "task_info",
    "task_error",
    # Configuration management
    "load_config",
    "get_config_value",
    "save_config",
    "list_config_files",
    "get_project_root",
]
