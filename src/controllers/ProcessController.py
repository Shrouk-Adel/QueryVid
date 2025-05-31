from .BaseController import BaseController
from langchain_community.document_loaders import TextLoader
from .VidoPathController import VideoPathController
from moviepy import VideoFileClip
import os 

class ProcessController(BaseController):
    def __init__(self,project_id):
        super().__init__()
        self.project_id =project_id

    def get_audio_from_vedio(self,file_id:str):
           
           file_dir =VideoPathController().get_file_dir(video_id=self.project_id)
           video_path =os.path.join(file_dir,file_id)
           video =VideoFileClip(video_path)

           audio_file_dir=os.path.join(self.audio_dir,self.project_id)

           if not os.path.exists(audio_file_dir):
                os.makedirs(audio_file_dir)

           full_audio_path =os.path.join(audio_file_dir ,'audio_'+self.project_id+'.wav')
           video.audio.write_audiofile(full_audio_path)

           return full_audio_path

    