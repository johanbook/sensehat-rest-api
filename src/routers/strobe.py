from fastapi import APIRouter
from ..skills import Strobe

router = APIRouter(prefix="/strobe")


strobe = Strobe()


@router.post("/start")
def start_strobe(color: str):
    """Starts a strobe effect"""
    global strobe
    strobe.start()
    return ""


@router.post("/stop")
def stop_strobe():
    """Stops the strobe effect"""
    global strobe
    strobe.stop()
    return ""
