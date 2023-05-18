import os
import sys
from typing import Union
from fastapi import FastAPI
from pydantic import Json

from .bridge.Bridge import request_aqi, request_forecast

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}   


@app.get("/get/current_forecast")
async def get_current_forecast(lat: str | None = None, lon: str | None = None, zip_code: int | None = None) -> dict: 
    res = await request_forecast(lat, lon, zip_code)
    return res


@app.get("/get/air_quality")
async def get_current_aqi(lat:str|None=None, lon:str|None=None, zip_code:int|None=None) -> dict:
    res = await request_aqi(lat, lon, zip_code)
    return res
