from pydantic import BaseModel,Field
from typing import Optional
from bson.objectid import ObjectId


class ChunkData(BaseModel):
    id :Optional[ObjectId]=Field(alias='_id')
    chunk_text:str=Field(...,)
    chunk_metadata:dict
    chunk_project_id :ObjectId
    chunk_order:int =Field(...,gt=0)

    class Config:
        arbitrary_types_allowed =True

