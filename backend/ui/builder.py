UI_TEMPLATES = {
    "sap_mode": ["dashboard", "analytics", "operations"],
    "notion_mode": ["pages", "blocks", "agents"],
    "figma_mode": ["drag_drop", "layout_engine"]
}

def render_ui(role):
    return UI_TEMPLATES.get(role, "default_ui")
