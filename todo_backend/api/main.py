from fastapi import FastAPI
from api.routers import task, done
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(task.router)
app.include_router(done.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)