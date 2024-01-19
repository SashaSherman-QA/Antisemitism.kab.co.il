import logging

logger = None


def setup_logger():
    global logger
    if logger is None:
        logger = logging.getLogger(__name__)
        file_handler = logging.FileHandler('logfile.log')
        logger.addHandler(file_handler)
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(formatter)
        # logger.setLevel(logging.INFO)  # Add to log file: info and above (error, critical)
        logger.setLevel(logging.WARNING)
    return logger
