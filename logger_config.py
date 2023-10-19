import logging
import sys
import os
from logging.handlers import TimedRotatingFileHandler
from config import config

if not os.path.exists('logs'):
    os.makedirs('logs')


def setup_logger(log_file='logs/app.log'):
    level = f'{config["log_level"]}'
    logger = logging.getLogger()
    logger.setLevel(level)

    formatter = logging.Formatter(
        '%(asctime)s - [%(levelname)s] - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s')

    file_handler = TimedRotatingFileHandler(
        log_file, when="midnight", interval=1, backupCount=7)
    file_handler.suffix = "%Y-%m-%d.log"
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


logger = setup_logger()
