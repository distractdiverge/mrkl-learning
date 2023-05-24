import pytest
from unittest.mock import patch
from ...services.logging import ConsoleLogger, LogLevel

def test_log():
    logger = ConsoleLogger()
    with patch('builtins.print') as mock_print:
        logger.log(LogLevel.INFO, "Test message")
        mock_print.assert_called_once_with('[INFO]: Test message')

def test_debug():
    logger = ConsoleLogger()
    with patch('builtins.print') as mock_print:
        logger.debug("Test message")
        mock_print.assert_called_once_with('[DEBUG]: Test message')

def test_info():
    logger = ConsoleLogger()
    with patch('builtins.print') as mock_print:
        logger.info("Test message")
        mock_print.assert_called_once_with('[INFO]: Test message')

def test_warn():
    logger = ConsoleLogger()
    with patch('builtins.print') as mock_print:
        logger.warn("Test message")
        mock_print.assert_called_once_with('[WARN]: Test message')

def test_error():
    logger = ConsoleLogger()
    with patch('builtins.print') as mock_print:
        logger.error("Test message")
        mock_print.assert_called_once_with('[ERROR]: Test message')
