from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Hello from my Notes API!"
    }


@app.get("/notes")
def get_notes():
    return {
        "notes": [
            "Learn deployment",
            "Learn GitHub",
            "Deploy Kivora"
        ]
    }
