import os
from typing import Union
from fastapi import FastAPI
import httpx
from dotenv import load_dotenv
from pydantic import Json

app = FastAPI()

load_dotenv()

COUNTRY_CODE = 'us'
api_key = os.getenv('API_KEY')
URL = f'https://api.openweathermap.org/data/2.5/weather?zip=43219,{COUNTRY_CODE}&appid={api_key}'
URL1 = f'http://api.openweathermap.org/data/2.5/air_pollution?lat=50&lon=50&appid={api_key}'

@app.get("/")
def read_root():
    return {"Hello": "World"}


async def request_forecast():
    async with httpx.AsyncClient() as client:
        task = await client.get(URL)
        return task.json()


async def request_aqi():
    async with httpx.AsyncClient() as client:
        task = await client.get(URL1)
        return task.json()     


@app.get("/get/current_forecast")
async def get_current_forecast(lat: str, lon: str) -> dict: 
    res = await request_forecast()
    return res


@app.get("/get/air_quality")
async def get_current_aqi() -> dict:
    res = await request_aqi()
    return res
