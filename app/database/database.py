from pytest_mock_resources import create_mongo_fixture
import os
import sys
from app.bootstrap.logger import logger


class Database:

    @staticmethod
    def getCursor():
        try:
            if os.getenv("ENV") == "test":
                logger.info("TEST MODE Connecting to database...")
                logger.info("TEST MODE Connected to database")
                return create_mongo_fixture()
        except Exception as e:
            logger.error(f"I can't establish connection with database: {e}")
            sys.exit(1)
