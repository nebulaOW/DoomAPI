from typing import List

import asyncpg
import databases
import sqlalchemy
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import urllib

import models

app = FastAPI()
DATABASE_URL = (
    f"postgresql://"
    f"{os.environ['PSQL_USER']}:"
    f"{os.environ['PSQL_PASSWORD']}@"
    f"{os.environ['PSQL_HOST']}:"
    f"{os.environ['PSQL_PORT']}/"
    f"{os.environ['PSQL_DATABASE']}"
)


#
#
# metadata = sqlalchemy.MetaData()
#
# notes = sqlalchemy.Table(
#     "notes",
#     metadata,
#     sqlalchemy.Column("map_code", sqlalchemy.String, primary_key=True),
#     sqlalchemy.Column("map_type", sqlalchemy.String),
#     sqlalchemy.Column("completed", sqlalchemy.Boolean),
# )
#
#
#
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/submit/map/")
async def add_map(_map: models.Map):
    connection = await asyncpg.create_pool(DATABASE_URL)
    async with connection.acquire() as conn:
        async with conn.transaction():
            await conn.execute(
                """
                INSERT INTO maps(map_code, map_type, map_name, "desc")
                VALUES ('TEST', $1,'Hanamura', 'tesxt desc');
                """, ["Framework"]
            )
            await conn.execute(
                """
                INSERT INTO map_creators(creator_id, map_code) VALUES (0, 'TEST');
                """
            )
    return _map
