from fastapi import FastAPI
from app.upload import router as upload_router
from app.chat import router as chat_router

app = FastAPI(title="Document Q&A API")

app.include_router(upload_router)
app.include_router(chat_router)

@app.get("/")
def root():
    return {"status": "Document Q&A API running"}
