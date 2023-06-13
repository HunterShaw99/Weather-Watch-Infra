
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
            url = f'https://api.openweathermap.org/data/2.5/weather?zip={zip_code}&appid={api_key}&units=imperial'
        else:
            url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=imperial'
        task = await client.get(url)
        return task.json()


async def request_aqi(lat=None, lon=None, zip_code=None):
    async with httpx.AsyncClient() as client:
        if zip_code:
            url = f'http://api.openweathermap.org/data/2.5/air_pollution?zip={zip_code}&appid={api_key}&units=imperial'
        else:
            url = f'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}&units=imperial'
        task = await client.get(url)
        return task.json() 