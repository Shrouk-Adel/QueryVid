from .BaseDataModel import BaseDataModel
from .Enums.DB_Enum import DBEnum
from .schemesdb.chunk_data import ChunkData
from pymongo import InsertOne # operation
from bson.objectid import ObjectId

class ChunkDataModel(BaseDataModel):
    def __init__(self,db_client:object):
        super().__init__(db_client=db_client)
        self.collection =self.db_client[DBEnum.CHUNK_COLLECTION_NAME.value]

    async def insert_chunk(self,chunk:ChunkData):
        result =await self.collection.insert_one(
            chunk.model_dump(by_alias=True,exclude_unset=True)
        )

        chunk =result._id
        return chunk
    async def get_chunk(self,chunk_id:str):
        reco =self.collection.find_one(
            {
                '_id':ObjectId(chunk_id)
            }
        )

        if reco is None:
            return None

        return ChunkData(**reco)
    
    async def insert_many_chunks(self,chunks:list,batch_size=100):

        for i in range (0,len(chunks),batch_size):
            batch =chunks[i:i+batch_size]

            operations =[
                InsertOne(chunk.model_dump())
                for chunk in batch
            ]

            await self.collection.bulk_write(operations)

        return len(chunks)
    
    async def delete_chunks_by_project_id(self,project_id:ObjectId):
        res=await self.collection.delete_many({
            'chunk_project_id':project_id
        })

        return res.deleted_count





      