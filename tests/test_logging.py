import unittest
import logging
from logging_module.logger import setup_logger

class TestLogging(unittest.TestCase):
    def test_logger_setup(self):
        logger = setup_logger()
        self.assertIsInstance(logger, logging.Logger)
        self.assertEqual(logger.name, 'NetworkDebuggingTool')
        self.assertEqual(len(logger.handlers), 2)  # File and console handlers

    def test_logger_levels(self):
        logger = setup_logger(log_level=logging.DEBUG)
        self.assertEqual(logger.level, logging.DEBUG)

        logger = setup_logger(log_level=logging.INFO)
        self.assertEqual(logger.level, logging.INFO)

if __name__ == '__main__':
    unittest.main()