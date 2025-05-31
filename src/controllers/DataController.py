from .BaseController import BaseController
from .VidoPathController import VideoPathController
from fastapi import UploadFile
from models import ResponseSingal
import re
import os 
class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.size_scale =1048576

    def validate_data(self,video:UploadFile,video_id:str):
        video_type =video.content_type
        video_size =video.size
        

        if video_type not in self.App_settings.FILE_ALLOWED_TYPES:
            return False,ResponseSingal.FILE_TYPE_NOT_VALID.value
        
        if video_size > self.App_settings.FILE_MAX_SIZE * self.size_scale:
            return False,ResponseSingal.FILE_SIZE_EXCEEDED.value
        
        return True,ResponseSingal.FILE_UPLOADED_SUCCSESS
    
    def process_vedio_name(self,video:UploadFile,video_id:str):
        cleaned_name =self.clean_name_vedio(vedio=video)
        file_path =VideoPathController().get_file_dir(video_id=video_id,video=video)
        random_key =BaseController().genrate_random_names()
        cleaned_file_path =os.path.join(
            file_path,
            random_key+'_'+cleaned_name
        )

        return cleaned_file_path,random_key+'_'+cleaned_name

    def clean_name_vedio(self,vedio:UploadFile):
        orignal_vedio_name=vedio.filename
        # remove any special character except _ or .
        cleaned_name =re.sub(r'[^\w.]','',orignal_vedio_name.strip())
        cleaned_name =cleaned_name.replace(" ",'_')

        return cleaned_name
