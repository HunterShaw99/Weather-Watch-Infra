from fastapi import FastAPI
from pydantic import Json

from .routers import weather
from .routers import user_creation
app = FastAPI()

app.include_router(weather.weather_router)
app.include_router(user_creation.usr_router)
@app.get("/")
def read_root():
    return {"Hello": "World"}   


