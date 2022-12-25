import time
from fastapi import FastAPI

from src.routers import alarm, strobe


app = FastAPI()
app.include_router(alarm.router)
app.include_router(strobe.router)
