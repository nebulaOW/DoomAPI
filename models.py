from pydantic import BaseModel


class Map(BaseModel):
    map_code: str
    map_type: list[str]
    map_name: str
    desc: str
    creators: list[int]

