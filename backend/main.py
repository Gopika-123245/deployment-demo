
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow our local frontend to communicate with the backend
origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
