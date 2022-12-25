from fastapi import APIRouter
from ..skills import Alarm

router = APIRouter(prefix="/alarm")


alarm = Alarm()


@router.post("/start")
def start_alarm():
    """Starts  blinking in red"""
    global alarm
    alarm.start()
    return ""


@router.post("/stop")
def stop_alarm():
    """Stops  blinking"""
    global alarm
    alarm.stop()
    return ""
