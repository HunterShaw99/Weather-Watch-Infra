import os
from typing import Any
from fastapi import APIRouter
from datetime import datetime as dt
import uuid
import psycopg2

from ..models.usr_data import usr_in, usr_out

usr_router = APIRouter()

@usr_router.post('/account_creation/', tags=['User'], response_model=usr_out)
async def post_user(usr_details: usr_in) -> Any: 
    conn = psycopg2.connect(dbname=os.getenv('POSTGRES_DB'), user=os.getenv('POSTGRES_USER'), password=os.getenv('POSTGRES_PASSWORD'), host=os.getenv('POSTGRES_HOST_LOCAL'), port=os.getenv('POSTGRES_PORT'))
    cur = conn.cursor()
    cur.execute('INSERT INTO app.users("user_email", "f_name", "l_name","phone_num","create_date", "u_GUID") VALUES (%s,%s,%s,%s,%s,%s)',
                (usr_details.user_email, usr_details.f_name, usr_details.l_name, usr_details.phone_num, dt.now(), uuid.uuid4().hex))
    conn.commit()
    cur.close()
    conn.close()
    return usr_details
    
