
import os
from typing import Union
from dotenv import load_dotenv
import httpx


load_dotenv()

COUNTRY_CODE = 'us'
api_key = os.getenv('API_KEY')
        

async def request_forecast(lat=None, lon=None, zip_code=None):
    async with httpx.AsyncClient() as client:
        if zip_code:
            url = f'https://api.openweathermap.org/data/2.5/weather?zip={zip_code},{COUNTRY_CODE}&appid={api_key}'
        else:
            url = f''
        task = await client.get(url)
        return task.json()


async def request_aqi(lat=None, lon=None, zip_code=None):
    async with httpx.AsyncClient() as client:
        url = f'http://api.openweathermap.org/data/2.5/air_pollution?lat=50&lon=50&appid={api_key}'
        task = await client.get(url)
        return task.json() 