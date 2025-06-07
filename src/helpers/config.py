from pydantic_settings import BaseSettings

class Setttings(BaseSettings):
    APP_NAME:str
    VERSION:str
    FILE_ALLOWED_TYPES:list
    FILE_MAX_SIZE:int
    CHUNK_SIZE:int
    GROK_API_KEY:str
    STT_LLM:str
    class Config:
        env_file ='.env'

def get_settings():
    return Setttings()