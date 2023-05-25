from enum import Enum
from abc import ABC, abstractmethod

class LogLevel(Enum):    
    DEBUG = 3
    INFO = 2
    WARN = 1
    ERROR = 0

class AbstractLogger(ABC):
    @abstractmethod
    def log(self, level:LogLevel, message:str) -> None:
        pass

    def debug(self, message:str) -> None:
        return self.log(LogLevel.DEBUG, message)

    def info(self, message:str) -> None:
        return self.log(LogLevel.INFO, message)

    def warn(self, message:str) -> None:
        return self.log(LogLevel.WARN, message)

    def error(self, message:str) -> None:
        return self.log(LogLevel.ERROR, message)

class ConsoleLogger(AbstractLogger):
    def log(self, level:LogLevel, message:str) -> None:
        print("[{0}]: {1}".format(level, message))