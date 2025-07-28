from fastapi import FastAPI
from app.database import engine
from app import models
from app.routes import user, eco, challenge, biome, leaderboard

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="EcoVerse API")

app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(eco.router, prefix="/eco", tags=["Eco Tasks"])
app.include_router(challenge.router, prefix="/challenges", tags=["Daily Challenges"])
app.include_router(biome.router, prefix="/biome", tags=["Biome"])
app.include_router(leaderboard.router, prefix="/leaderboard", tags=["Leaderboard"])
