import logging
import os
from datetime import datetime

def setup_logger(log_level=logging.INFO, log_file=None):
    logger = logging.getLogger('NetworkDebuggingTool')
    logger.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    if log_file:
        # Create the logs directory if it doesn't exist
        log_dir = os.path.dirname(log_file)
        os.makedirs(log_dir, exist_ok=True)
        
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger

# Use an absolute path for the log file
log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'logs')
log_file = os.path.join(log_dir, f"network_debugging_tool_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
logger = setup_logger(log_file=log_file)