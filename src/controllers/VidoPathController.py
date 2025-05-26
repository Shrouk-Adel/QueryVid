from .BaseController import BaseController
import os 

class VideoPathController(BaseController):

    def get_file_dir(self,video_id:str):
        video_dir =os.path.join(self.files_dir,video_id)

        if not os.path.exists(video_dir):
            os.makedirs(video_dir)

        return video_dir