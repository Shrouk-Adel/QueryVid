from .BaseDataModel import BaseDataModel
from .schemesdb.project import Project
from .Enums.DB_Enum import DBEnum

class ProjectDataModel(BaseDataModel):
    def __init__(self,db_clinet:object):
        super().__init__(db_client=db_clinet)
        self.collection =self.db_client[DBEnum.PROJECT_COLLECTION_NAME.value]
    
    async def insert_project(self,project:Project):
        result =await self.collection.insert_one(
            project.model_dump(by_alias=True,exclude_unset=True)
        )

        project =result._id

        return project
    
    async def get_or_insert_project(self,project_id:str):
        result = await self.collection.find_one(
            {
               'project_id':project_id
            }
        )

        if result is None:
            project =Project(
                project_id=project_id
                )
            
            reco =await self.insert_project(project=project)

            return Project(**reco)
        
        return Project(**result)
    

    async def get_all_projects(self,page:int,page_size:int =10):
        total_documents =await self.collection.count_documents({})

        total_pages =total_documents// page_size

        if total_documents % page_size !=0:
            total_pages +=1

        
        cursor =self.collection.find().skip(page-1*page_size).limit(page_size)

        projects=[]
        async for document in cursor:
            projects.append(
                Project(**document)
            )

        return projects,total_pages
