import uvicorn
from fastapi import FastAPI
from pysondb import db
from routers import lists_router, tasks_router
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

origins = [
    "http://localhost.com:3000",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows all origins
    allow_credentials=True,
    allow_methods=["*"], # Allows all methods
    allow_headers=["*"], # Allows all headers
)

app.include_router(lists_router.router)
app.include_router(tasks_router.router)


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
