RULES = {
    "EU": ["GDPR", "AI_ACT"],
    "US": ["CCPA", "FTC"],
    "CHINA": ["PIPL"]
}

def validate(region, action):
    return {
        "region": region,
        "action": action,
        "status": "compliant"
    }
