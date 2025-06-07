from pydantic import BaseModel ,Field
from typing import Optional

class ProcessRequest(BaseModel):

    file_id:str =Field(...,)
    chunk_size :Optional[int] =200
    chunk_overlap:Optional[int]=50
    do_reset:Optional[int]=0