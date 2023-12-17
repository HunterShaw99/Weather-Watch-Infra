
import os
from typing import Union
from dotenv import load_dotenv
import httpx

load_dotenv()

COUNTRY_CODE = 'us'
api_key = os.getenv('API_KEY')
headers = {'User-Agent': 'weather-watch.app, huntershaw0@gmail.com'}

@staticmethod
async def request_forecast(lat, lon):
    async with httpx.AsyncClient(headers=headers) as client:
        url_gridpoints = f'https://api.weather.gov/points/{lat},{lon}'
        proxy = await client.get(url_gridpoints)
        url_forecast = proxy.json()
        url_forecast = url_forecast['properties']['forecastHourly']
        proxy = await client.get(url_forecast)
        return [proxy.json(), proxy.status_code]

@staticmethod
async def request_aqi(lat=None, lon=None, zip_code=None):
    async with httpx.AsyncClient() as client:
        if zip_code:
            url = f'http://api.openweathermap.org/data/2.5/air_pollution?zip={zip_code}&appid={api_key}&units=imperial'
        else:
            url = f'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}&units=imperial'
        task = await client.get(url)
        return task.json() 