from .BaseController import BaseController
from fastapi import UploadFile
from models import ResponseSingal

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