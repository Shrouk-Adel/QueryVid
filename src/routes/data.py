from fastapi import APIRouter,Depends,UploadFile,status
from controllers import DataController



data_router =APIRouter(
    prefix='/api/v1/data',
    tags=['api_v1','data']
)


@data_router.post('/upload/{video_id}')
async def upload_data(video_id:str,video:UploadFile):
        
        # validate video 
        is_valid,signal =DataController.validate_data(video=video,video_id=video_id)
        
        if not is_valid:  
            status_code =status.HTTP_400_BAD_REQUEST
            return {
                'status':status_code,
                'signal':signal
            }
        
        return{
              'signal':signal
        }