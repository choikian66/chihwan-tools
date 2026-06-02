import os
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

load_dotenv()

from routers import branch_diagnosis, manual_chat


@asynccontextmanager
async def lifespan(app: FastAPI):
    from utils.migrate import run_migrations
    run_migrations()
    yield


app = FastAPI(title="Chihwan Tools API", lifespan=lifespan)

FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL, "http://localhost:5173", "http://localhost:5174"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(GZipMiddleware, minimum_size=1000)

app.include_router(branch_diagnosis.router, prefix="/fde-api/diagnosis", tags=["diagnosis"])
app.include_router(manual_chat.router, prefix="/fde-api/manual", tags=["manual"])


@app.get("/fde-api/health")
def health():
    return {"status": "ok"}
