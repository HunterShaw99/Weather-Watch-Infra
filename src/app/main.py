from fastapi import FastAPI
from pydantic import Json

from .routers import weather

app = FastAPI()

app.include_router(weather.weather_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}   


