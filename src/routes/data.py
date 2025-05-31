from fastapi import APIRouter,Depends,UploadFile,status
from fastapi.responses import JSONResponse
from controllers import DataController,VideoPathController
import aiofiles
from helpers import Setttings,get_settings
import os 


data_router =APIRouter(
    prefix='/api/v1/data',
    tags=['api_v1','data']
)

App_settings =get_settings()
@data_router.post('/upload/{video_id}')
async def upload_data(video_id:str,video:UploadFile):
        
        # validate video 
        is_valid,signal =DataController().validate_data(video=video,video_id=video_id)
        
        if not is_valid:  
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content ={
                      'signal':signal
                }
            
            )
        
        file_path,file_id =DataController().process_vedio_name(video=video,video_id=video_id)

        async with aiofiles.open(file_path,'wb')  as f:
              while chunk:=await video.read(App_settings.CHUNK_SIZE):
                    await f.write(chunk)
           
        
        return{
              'signal':signal,
              'file_id':file_id
        }


@app_router('/process/{project_id}')
async def process_vedio(project_id:str,file_id:str):
    file_content =