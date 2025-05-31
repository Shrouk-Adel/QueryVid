from .BaseController import BaseController
from langchain_community.document_loaders import 

class ProcessController(BaseController):
    def __init__(self,project_id):
        super().__init__()
        self.project_id =project_id

    