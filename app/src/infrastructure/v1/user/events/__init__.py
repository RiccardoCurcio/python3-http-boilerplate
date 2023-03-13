from app.src.domain.abc.event import Event
from app.src.infrastructure.v1.user.exceptions.eventsException import UserEventExcepion
import asyncio
from typing import Union
from app.bootstrap.logger import logger
from threading import Thread
from app.src.infrastructure.v1.user.entities import User
from app.src.infrastructure.v1.user.events.actions.create_user_action import CreateUserAction
from app.src.infrastructure.v1.user.events.actions.read_user_action import ReadUserAction
from app.src.infrastructure.v1.user.events.actions.read_users_action import ReadUsersAction
from app.src.infrastructure.v1.user.events.actions.update_user_action import UpdateUserAction
from app.src.infrastructure.v1.user.events.actions.delete_user_action import DeleteUserAction


class UserEvent(Event):
    """[summary]

    Args:
        Event ([type]): [description]
    """
    def __init__(self, eventName: str):
        """[summary]

        Args:
            eventName (str): [description]
        """
        self.__event = eventName
        self.__eventMapping = {
            "create_user_event": CreateUserAction,
            "read_user_event": ReadUserAction,
            "read_users_event": ReadUsersAction,
            "update_user_event": UpdateUserAction,
            "delete_user_event": DeleteUserAction
        }
        pass

    def dispatch(self, data: Union[User, list[User], None] = None) -> None:
        """[summary]

        Args:
            id (Union[str, None], optional): [description]. Defaults to None.
            data (dict, optional): [description]. Defaults to {}.

        Raises:
            userEventExcepion: [description]

        Returns:
            [type]: [description]
        """
        try:
            logger.info(f'start loop event {self.__event}')
            send_loop = asyncio.new_event_loop()
            t = Thread(target=run, args=(send_loop, self.__event, self.__eventMapping, data))
            t.start()
        except Exception as e:
            logger.error({"error": f"user dispatch {self.__event} : {e.__repr__}"}, exc_info=True)
            raise UserEventExcepion(e)
        return None


def run(loop, eventName: str, eventMapping: dict, data: Union[User, list[User], None] = None):
    """[summary]

    Args:
        loop ([type]): [description]
        eventName (str): [description]
        eventMapping (dict): [description]
        id (Union[str, None]): [description]
        data (dict): [description]
    """
    asyncio.set_event_loop(loop)
    eventMapping[eventName]().run(data=data)
    loop.close()
