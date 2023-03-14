from app.src.domain.abc.event import Event
from app.src.infrastructure.v1.placeholder.exceptions.eventsException import PlaceholderEventExcepion
import asyncio
from typing import Union
from app.bootstrap.logger import logger
from threading import Thread
from app.src.infrastructure.v1.placeholder.entities import Placeholder
from app.src.infrastructure.v1.placeholder.events.actions.create_placeholder_action import CreatePlaceholderAction
from app.src.infrastructure.v1.placeholder.events.actions.read_placeholder_action import ReadPlaceholderAction
from app.src.infrastructure.v1.placeholder.events.actions.read_placeholders_action import ReadPlaceholdersAction
from app.src.infrastructure.v1.placeholder.events.actions.update_placeholder_action import UpdatePlaceholderAction
from app.src.infrastructure.v1.placeholder.events.actions.delete_placeholder_action import DeletePlaceholderAction


class PlaceholderEvent(Event):
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
            "create_placeholder_event": CreatePlaceholderAction,
            "read_placeholder_event": ReadPlaceholderAction,
            "read_placeholders_event": ReadPlaceholdersAction,
            "update_placeholder_event": UpdatePlaceholderAction,
            "delete_placeholder_event": DeletePlaceholderAction
        }
        pass

    def dispatch(self, data: Union[Placeholder, list[Placeholder], None] = None) -> None:
        """[summary]

        Args:
            id (Union[str, None], optional): [description]. Defaults to None.
            data (dict, optional): [description]. Defaults to {}.

        Raises:
            placeholderEventExcepion: [description]

        Returns:
            [type]: [description]
        """
        try:
            logger.info(f'start loop event {self.__event}')
            send_loop = asyncio.new_event_loop()
            t = Thread(target=run, args=(send_loop, self.__event, self.__eventMapping, data))
            t.start()
        except Exception as e:
            logger.error({"error": f"placeholder dispatch {self.__event} : {e.__repr__}"}, exc_info=True)
            raise PlaceholderEventExcepion(e)
        return None


def run(loop, eventName: str, eventMapping: dict, data: Union[Placeholder, list[Placeholder], None] = None):
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
