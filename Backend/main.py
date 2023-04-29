from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Set up CORS
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:5500",
    "http://127.0.0.1:5500",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello"}

# Define the endpoint
@app.post("/message")
async def receive_message(message: dict):
    print(f"Received message: {message}")
    return {"message": "Message received!"}