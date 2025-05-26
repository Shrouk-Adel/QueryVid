from helpers import Setttings,get_settings
from fastapi import Depends
import random
import string

class BaseController:
    def __init__(self):
        self.App_settings =get_settings()
        

    def genrate_random_names(self,length=12):
        return ''.join(random.choices(string.ascii_lowercase,string.digits,k=length))
