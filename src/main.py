import os
from typing import Union
from fastapi import FastAPI
import httpx
from dotenv import load_dotenv

app = FastAPI()

load_dotenv()

COUNTRY_CODE = 'us'
api_key = os.getenv('API_KEY')
URL = f'https://api.openweathermap.org/data/2.5/weather?zip=43219,{COUNTRY_CODE}&appid={api_key}'


@app.get("/")
def read_root():
    return {"Hello": "World"}


async def request_forecast():
    async with httpx.AsyncClient() as client:
        task = await client.get(URL)
        response = task.json()
        return response


@app.get("/get/current_forecast")
async def read_item():
    res = await request_forecast()
    return {'test': res}
