from routes.bas import base_router
from fastapi import FastAPI
from routes.data import data_router
from motor.motor_asyncio import AsyncIOMotorClient
from contextlib import asynccontextmanager
from helpers import Setttings,get_settings

#create event
@asynccontextmanager
def lifspan(app:FastAPI):
  app_settings =get_settings()

  # when start app
  app.mongo_conn =AsyncIOMotorClient(app_settings.MONGO_URL)
  app.db_client =app.mongo_conn[app_settings.MONGODB_DATABASE]

  yield
  # when shutdown app
  app.mongo_conn.close()


app =FastAPI(lifespan=lifspan)

app.include_router(base_router)
app.include_router(data_router)

