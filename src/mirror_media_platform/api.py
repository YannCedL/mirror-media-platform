import os
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from genesis_core import ResultContract
from .engine import analyze_media

app = FastAPI(
    title="MIRROR Media Platform API",
    description="Plateforme Média, Vérification & Forensics 360°",
    version="1.0.0"
)

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates", "index.html")

@app.get("/", response_class=HTMLResponse)
def index():
    # sert la page d'accueil de la plateforme media
    if os.path.exists(TEMPLATE_PATH):
        with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>MIRROR Platform API - Interface non trouvee</h1>"

@app.get("/health")
def health():
    return {"status": "ok", "platform": "MIRROR", "version": "1.0.0"}

@app.get("/api/v1/analyze", response_model=ResultContract)
def analyze(filepath: str = Query("sample_file.jpg")):
    return analyze_media(filepath)

# upload endpoint added
