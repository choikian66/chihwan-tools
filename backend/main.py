import os
from contextlib import asynccontextmanager
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.staticfiles import StaticFiles

load_dotenv()

from routers import branch_diagnosis, manual_chat


@asynccontextmanager
async def lifespan(app: FastAPI):
    from utils.migrate import run_migrations
    run_migrations()
    yield


app = FastAPI(title="Chihwan Tools API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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


# 빌드된 React 정적 파일 서빙 (배포 환경)
_static = Path(__file__).parent / "static"
if _static.exists():
    app.mount("/", StaticFiles(directory=str(_static), html=True), name="static")
