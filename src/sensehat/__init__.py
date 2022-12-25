try:
    from .sensehat import SenseHatInterface
except ImportError:
    from .sensehat_mock import SenseHatInterface  # type: ignore

sensehat = SenseHatInterface()
