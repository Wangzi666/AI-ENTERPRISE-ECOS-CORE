COURSES = {
    "seo": ["basic", "advanced", "ai-assisted seo"],
    "legal": ["ip protection", "complaints automation"],
    "ved": ["logistics AI", "cost optimization"]
}

def enroll(user, course):
    return {
        "user": user,
        "course": course,
        "status": "learning started"
    }
