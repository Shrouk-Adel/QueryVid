from fastapi import APIRouter,Depends,UploadFile,status,Request
from fastapi.responses import JSONResponse
from controllers import DataController,ProcessController
import aiofiles
from helpers import Setttings,get_settings
import os 
from .shemes import ProcessRequest
from models import ProjectDataModel,ChunkDataModel
from models import ChunkData,Project,ResponseSingal


data_router =APIRouter(
    prefix='/api/v1/data',
    tags=['api_v1','data']
)

App_settings =get_settings()

@data_router.post('/upload/{project_id}')
async def upload_data(request:Request,project_id:str,file:UploadFile):
        # validate video 
        is_valid,signal =DataController().validate_data(file=file)
        
        if not is_valid:  
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content ={
                      'signal':signal
                }
            
            )
        

        # store project in mongodb 
        project_model =ProjectDataModel(
              db_clinet=request.app.db_client
        )

        project =project_model.get_or_insert_project(
              project_id=project_id
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
async def process_vedio(request:Request,project_id:str,process_request:ProcessRequest):
    file_id =process_request.file_id
    chunk_size =process_request.chunk_size
    chunk_overlap =process_request.chunk_overlap
    do_reset =process_request.do_reset


    chunk_model =ChunkDataModel(
          db_client=request.app.db_client
    )
    project_model =ProjectDataModel(
          db_clinet=request.app.db_client
    )

    project =project_model.get_or_insert_project(
          project_id =project_id
    )


    if do_reset !=0:
          _=chunk_model.delete_chunks_by_project_id(
                project_id =project.id
          )


    # split data into chunks 
    chunks =ProcessController().get_chunks_from_content(file_id=file_id,
                                                        project_id=project_id,
                                                        chunk_size=chunk_size,
                                                        chunk_overlap=chunk_overlap
                                                        )
  

    if chunks is None or len(chunks) is None:
          return JSONResponse(
                status_code =status.HTTP_400_BAD_REQUEST
                content ={
                      'signal':ResponseSingal.FILE_PROCESSD_FALID
                }
          )   
    
    # store file chunks in db

    chunks_list =[
          ChunkData(
                chunk_order=i+1,
                chunk_text=chunk.page_content,
                chunk_metadata =chunk.metadata,
                chunk_project_id =project._id

          )
          for i,chunk in enumerate(chunks)
    ]

    no_chunks= await chunk_model.insert_many_chunks(
          chunks =chunks_list
          )
    

    return JSONResponse(
          content={
          'signal':ResponseSingal.FILE_PROCESSD_SUCCESS.value,
          "no_chunks":no_chunks
          }
      )

