from fastapi import FastAPI
from routers import documents

app = FastAPI(
    title="RAG Backend"
)
app.include_router(documents.router)

@app.get("/health")
def health():
    return {"status": "ok"}