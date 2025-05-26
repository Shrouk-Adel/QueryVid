from pydantic_settings import BaseSettings


class Setttings(BaseSettings):
    APP_NAME:str
    VERSION:str
    FILE_ALLOWED_TYPES:list
    FILE_MAX_SIZE:int

    class Config:
        env_file ='.env'

def get_settings():
    return Setttings()