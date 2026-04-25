from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import scan, products, health_score, image_scan
from app.core.config import settings

app = FastAPI(
    title="SKI — Scan Karega India API",
    version="0.1.0",
    description="AI-powered food quality monitoring platform",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(scan.router,         prefix="/api/scan",         tags=["Scan"])
app.include_router(products.router,     prefix="/api/products",     tags=["Products"])
app.include_router(health_score.router, prefix="/api/health-score", tags=["Health Score"])
app.include_router(image_scan.router,   prefix="/api/image-scan",   tags=["Image Scan"])

@app.get("/")
def root():
    return {"message": "SKI API is running", "version": "0.1.0", "docs": "/docs"}
