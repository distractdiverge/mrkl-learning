import pytest
from io import StringIO
from contextlib import redirect_stdout

from mrkl_learning.services.logging import AbstractLogger, ConsoleLogger, LogLevel

def test_abstract_logger_methods():
    with pytest.raises(TypeError):
        abstract_logger = AbstractLogger()

@pytest.fixture()
def console_logger():
    return ConsoleLogger()

def test_console_logger_log(console_logger):
    message = "Test log message"

    with StringIO() as buffer, redirect_stdout(buffer):
        console_logger.log(LogLevel.DEBUG, message)
        output = buffer.getvalue().strip()

    expected_output = "[{}]: {}".format(LogLevel.DEBUG, message)

    assert output == expected_output

def test_console_logger_debug(console_logger):
    message = "Test debug message"
    
    with StringIO() as buffer, redirect_stdout(buffer):
        console_logger.debug(message)
        output = buffer.getvalue().strip()
        
    expected_output = "[{}]: {}".format(LogLevel.DEBUG, message)
    
    assert output == expected_output


def test_console_logger_info(console_logger):
    message = "Test info message"
    
    with StringIO() as buffer, redirect_stdout(buffer):
        console_logger.info(message)
        output = buffer.getvalue().strip()
        
    expected_output = "[{}]: {}".format(LogLevel.INFO, message)
    
    assert output == expected_output


def test_console_logger_warn(console_logger):
    message = "Test warn message"
    
    with StringIO() as buffer, redirect_stdout(buffer):
        console_logger.warn(message)
        output = buffer.getvalue().strip()
        
    expected_output = "[{}]: {}".format(LogLevel.WARN, message)
    
    assert output == expected_output


def test_console_logger_error(console_logger):
    message = "Test error message"
    
    with StringIO() as buffer, redirect_stdout(buffer):
        console_logger.error(message)
        output = buffer.getvalue().strip()
        
    expected_output = "[{}]: {}".format(LogLevel.ERROR, message)
    
    assert output == expected_output