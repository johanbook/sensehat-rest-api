import time

from sense_hat import SenseHat  # type: ignore

from .interface import AbstractSensehatInterface


class SenseHatInterface(AbstractSensehatInterface):
    def __init__(self):
        self.sense_hat = SenseHat()

    def fill(self, color):
        self.sense_hat.clear(color)
