import os
import logging

import asyncio
from threading import Thread

# import datetime
# import traceback


handler = logging.StreamHandler()
handler.setFormatter(
    logging.Formatter(
        fmt="[%(asctime)s] %(levelname)s %(pathname)s line:%(lineno)d %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
)

logger = logging.getLogger("root")
logger.setLevel(logging.getLevelName(os.getenv("LOGGING_LEVEL", "INFO")))
logger.addHandler(handler)

logging.getLogger("asyncio").setLevel(os.getenv("LOGGING_LEVEL", "INFO"))


def eventLog(record):
    send_loop = asyncio.new_event_loop()
    t = Thread(target=run, args=(send_loop, record))
    t.start()
    return True


def run(loop, record):
    asyncio.set_event_loop(loop)
    # if record.levelname == "INFO":
    #     pass
    # if record.levelname == "DEBUG":
    #     pass
    # if record.levelname == "ERROR":
    #     # print(record.getMessage(), traceback.format_exc())
    #     pass
    # if record.levelname == "CRITICAL":
    #     pass
    loop.close()

    return True


logging.root.addFilter(eventLog)
