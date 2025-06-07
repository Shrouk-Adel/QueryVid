from fastapi import APIRouter,Depends,UploadFile,status
from fastapi.responses import JSONResponse
from controllers import DataController,ProcessController
import aiofiles
from helpers import Setttings,get_settings
import os 
from .shemes import ProcessRequest


data_router =APIRouter(
    prefix='/api/v1/data',
    tags=['api_v1','data']
)

App_settings =get_settings()

@data_router.post('/upload/{project_id}')
async def upload_data(project_id:str,file:UploadFile):
        
        # validate video 
        is_valid,signal =DataController().validate_data(file=file)
        
        if not is_valid:  
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content ={
                      'signal':signal
                }
            
            )
        
        file_path,file_id =DataController().process_file_name(file=file,project_id=project_id)

        async with aiofiles.open(file_path,'wb')  as f:
              while chunk:=await file.read(App_settings.CHUNK_SIZE):
                    await f.write(chunk)
           
        
        return{
              'signal':signal,
              'file_id':file_id
        }


@data_router.post('/process/{project_id}')
async def process_vedio(project_id:str,process_request:ProcessRequest):
    file_id =process_request.file_id
    chunk_size =process_request.chunk_size
    chunk_overlap =process_request.chunk_overlap

    chunks =ProcessController().get_chunks_from_content(file_id=file_id,
                                                        project_id=project_id,
                                                        chunk_size=chunk_size,
                                                        chunk_overlap=chunk_overlap
                                                        )

    return {
          'chunks':chunks
    }



     
