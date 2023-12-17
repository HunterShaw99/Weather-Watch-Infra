from fastapi import APIRouter, HTTPException, Header

from ..bridge.Bridge import request_aqi, request_forecast

weather_router = APIRouter()

@weather_router.get('/current_forecast/', tags=['Weather'])
async def get_current_forecast(lat:str|None=None, lon:str|None=None) -> dict: 
    res = await request_forecast(lat[:5], lon[:5])
    if res[1] != 200:
        raise HTTPException(status_code=404, detail="too many requests")
    return res[0]['properties']

@weather_router.get('/air_quality/', tags=['Weather'])
async def get_current_aqi(lat:str|None=None, lon:str|None=None, zip_code:int|None=None) -> dict:
    res = await request_aqi(lat, lon, zip_code)
    if res['status'] != 200:
        raise HTTPException(status_code=404, detail="too many requests")
    return res