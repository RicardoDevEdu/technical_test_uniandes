from fastapi import FastAPI

from app.dependencies.database import create_tables
from app.routes import migrations, starship, pilot

app = FastAPI(
    title="API new imperio starship",
    description="Full starship API list",
    version="1.0.0",
    lifespan=create_tables
)



app.include_router(migrations.router, prefix="/api/v1", tags=["Migration"])
app.include_router(starship.router, prefix="/api/v1", tags=["Starship"])
app.include_router(pilot.router, prefix="/api/v1", tags=["Pilot"])


@app.get("/")
async def root():
    return {"message": "starship API v1.0.0"}