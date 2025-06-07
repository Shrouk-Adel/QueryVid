from .BaseController import BaseController
from langchain_community.document_loaders import TextLoader,PyMuPDFLoader
from langchain_community.document_loaders import UnstructuredPowerPointLoader
from langchain_community.document_loaders import UnstructuredWordDocumentLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from .FilePathController import FilePathController
import os 
from models import ProcessEnum

class ProcessController(BaseController):
    def __init__(self):
        super().__init__()
    
    def get_ext_file (self,file_id:str):
        ext =os.path.splitext(file_id)[-1]
        return ext

    def get_content_from_file(self,file_id:str,project_id:str):
        file_dir =FilePathController().get_file_dir(project_id=project_id)
        file_path =os.path.join(file_dir,file_id)
        
        # detrmint type of docutment by extension
        ext =self.get_ext_file(file_id=file_id)
        
        if ext == ProcessEnum.TXT.value:
            loader =TextLoader(file_path=file_path,encoding='utf-8')
        if ext ==ProcessEnum.PDF.value:
            loader =PyMuPDFLoader(file_path=file_path)
        if ext in ProcessEnum.DOC.value:
            loader =UnstructuredWordDocumentLoader(file_path=file_path)

        if ext in ProcessEnum.PPT.value:
            loader =UnstructuredPowerPointLoader(file_path=file_path)
        
        return loader.load()
    

    def get_chunks_from_content(self,file_id:str,project_id:str,chunk_size=200,chunk_overlap=50):
        file_content =self.get_content_from_file(file_id=file_id,project_id=project_id)
        spliter =RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap =chunk_overlap,
            length_function =len
        )
        
        file_text =[
            rec.page_content
            for rec in file_content
        ]

        file_metadata=[
            rec.metadata
            for rec in file_content
        ]

        chunks =spliter.create_documents(
            file_text,
            metadatas=file_metadata
        )

        return chunks

    
