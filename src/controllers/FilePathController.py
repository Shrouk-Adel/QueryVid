from .BaseController import BaseController
import os 

class FilePathController(BaseController):

    def get_file_dir(self,project_id:str):
        file_dir =os.path.join(self.files_dir,project_id)

        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        
        
        return file_dir