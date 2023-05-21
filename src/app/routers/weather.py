from fastapi import APIRouter

from ..bridge.Bridge import request_aqi, request_forecast

weather_router = APIRouter()

@weather_router.get('/current_forecast/', tags=['Weather'])
async def get_current_forecast(lat: str | None = None, lon: str | None = None, zip_code: int | None = None) -> dict: 
    res = await request_forecast(lat, lon, zip_code)
    return res

@weather_router.get('/air_quality/', tags=['Weather'])
async def get_current_aqi(lat:str|None=None, lon:str|None=None, zip_code:int|None=None) -> dict:
    res = await request_aqi(lat, lon, zip_code)
    return res