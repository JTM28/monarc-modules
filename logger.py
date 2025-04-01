# logger.py
# dependencies: loguru>=0.6

from loguru import logger

def log(msg):
    logger.info(f"[monarc] {msg}")
