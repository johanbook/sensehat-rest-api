"""
Interface used for mocking SenseHat service
"""
import time

from .interface import AbstractSensehatInterface


class SenseHatInterface(AbstractSensehatInterface):
    def fill(self, color):
        print("Lighting up", color)
