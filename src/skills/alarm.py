from ..colors import EMPTY, RED
from ..sensehat import sensehat
from ..thread import create_thread


class Alarm:
    def __init__(self):
        self.color = EMPTY
        self.thread = None

    def start(self):
        self.thread = create_thread(self.callback)
        self.thread.start()

    def stop(self):
        if not self.thread:
            return
        self.thread.active = False
        self.thread = None

        sensehat.fill(EMPTY)

    def callback(self):
        if self.color is EMPTY:
            self.color = RED
        else:
            self.color = EMPTY

        sensehat.fill(self.color)
