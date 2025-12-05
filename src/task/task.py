"""
This is a module bbz
"""
from datetime import datetime

def new_task(description):
    """
    Constructor for new tasks
    """
    current_time = datetime.isoformat(datetime.now())
    task = {"description": description, "status": "todo", "createdAt": current_time}
    task["updatedAt"] = task["createdAt"]
    return task
