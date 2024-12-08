from fastapi import FastAPI

from app.routes import migrations

app = FastAPI(
    title="API new imperio starship",
    description="Full starship API list",
    version="1.0.0",
)

app.include_router(migrations.router, prefix="/api/migration/init", tags=["Migration"])


@app.get("/")
async def root():
    return {"message": "starship API v1.0.0"}