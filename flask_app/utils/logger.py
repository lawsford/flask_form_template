import logging


class _Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=_Singleton):
    """
    Logger class
    """
    def __init__(self, gunicorn=True):
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)
        if gunicorn:
            self._initialize_gunicorn_logger()

    def _initialize_gunicorn_logger(self):
        _gunicorn_logger = logging.getLogger("gunicorn.error")
        self.logger.handlers = _gunicorn_logger.handlers
        self.logger.setLevel(_gunicorn_logger.level)