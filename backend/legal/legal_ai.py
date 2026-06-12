def generate_complaint(case):
    return {
        "type": "IP violation",
        "case": case,
        "document": "AUTO PDF GENERATED",
        "status": "ready for submission"
    }

def calculate_damage(copies):
    return copies * 120
