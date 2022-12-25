import logging
import threading
import time

THREAD_SLEEP_TIME_IN_SECONDS = 0.5


def thread_loop(callback, sleeping_time):
    current_thread = threading.currentThread()
    while getattr(current_thread, "active", True):
        callback()
        time.sleep(sleeping_time)


def create_thread(callback, sleeping_time=THREAD_SLEEP_TIME_IN_SECONDS):
    thread = threading.Thread(target=thread_loop, args=(callback, sleeping_time))
    return thread
