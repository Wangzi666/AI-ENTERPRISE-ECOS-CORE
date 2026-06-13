import os

class Builder:

    def generate(self, plan):
        print("вљ™пёЏ GENERATING PROJECT")

        os.makedirs("backend/api", exist_ok=True)

        with open("backend/main.py", "w") as f:
            f.write(f'''
from fastapi import FastAPI

app = FastAPI(title="ECOS v1 Factory")

@app.get("/system")
def system():
    return {{
        "status": "running",
        "module": "{plan['entity']}",
        "target": "{plan['target']}"
    }}
''')


