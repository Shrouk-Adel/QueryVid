from helpers import Setttings,get_settings
from fastapi import Depends
import random
import string
import os 

class BaseController:
    def __init__(self):
        self.App_settings =get_settings()
        self.base_dir =os.path.dirname(os.path.dirname(__file__))
        self.files_dir =os.path.join(self.base_dir,'assets/files')

    def genrate_random_names(self,length=12):
        return ''.join(random.choices(string.ascii_lowercase,string.digits,k=length))
