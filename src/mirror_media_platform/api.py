from fastapi import FastAPI
from genesis_core import ResultContract
from .engine import analyze_media

app = FastAPI(title="Mirror Media Platform API", version="1.0.0")

@app.get("/health")
def health():
    return {"status": "ok", "engine": "Mirror"}

@app.get("/api/v1/analyze")
def analyze(filepath: str):
    return analyze_media(filepath)
