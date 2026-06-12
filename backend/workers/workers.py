WORKER_POOL = {
    "freelancer": ["seo_tasks", "content_tasks"],
    "agency": ["legal_tasks", "ved_tasks"]
}

def assign_task(worker_type, task):
    return {
        "worker": worker_type,
        "task": task,
        "status": "assigned"
    }
