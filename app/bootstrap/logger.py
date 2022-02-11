import logging
import os
# from app.bootstrap.env import loaded


handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(fmt='[%(asctime)s] %(levelname)s %(pathname)s line:%(lineno)d %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))

logger = logging.getLogger('root')
logger.setLevel(logging.getLevelName(os.getenv('LOGGING_LEVEL', 'INFO')))
logger.addHandler(handler)

logging.getLogger('asyncio').setLevel(logging.WARNING)
