from fastapi import FastAPI,APIRouter,Depends
from helpers import get_settings,Setttings
from models import ResponseSingal

base_router =APIRouter(
    prefix='/api/v1',
    tags=['api_v1']
)

App_settings = get_settings()

@base_router.get('/')
def welcome(App_settings:Setttings =Depends(get_settings)):

    App_Name =App_settings.APP_NAME
    App_version =App_settings.VERSION
    return {
        "App_Name":App_Name,
        "App_Version":App_version,
        "Signal":ResponseSingal.WELCOM_MESSAGE.value
    }