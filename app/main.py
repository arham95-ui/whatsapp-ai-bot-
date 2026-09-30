from fastapi import FastAPI
from app.api.webhook import router as webhook_router

app = FastAPI(title="WhatsApp AI Bot", version="1.0.0")

app.include_router(webhook_router, tags=["webhook"])

@app.get("/")
async def root():
    return {"status": "running", "service": "WhatsApp AI Bot"}

@app.get("/health")
async def health():
    return {"ok": True}