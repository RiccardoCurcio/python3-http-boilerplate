from app.src.events import Event, CompanyEventExcepion
import asyncio
import traceback
from typing import Union
from app.bootstrap.logger import logger
from threading import Thread
from app.src.events.company.actions.create_company_action import CreateCompanyAction
from app.src.events.company.actions.read_company_action import ReadCompanyAction
from app.src.events.company.actions.read_companies_action import ReadCompaniesAction
from app.src.events.company.actions.update_company_action import UpdateCompanyAction
from app.src.events.company.actions.delete_company_action import DeleteCompanyAction


class CompanyEvent(Event):
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
            "create_company_event": CreateCompanyAction,
            "read_company_event": ReadCompanyAction,
            "read_companies_event": ReadCompaniesAction,
            "update_company_event": UpdateCompanyAction,
            "delete_company_event": DeleteCompanyAction
        }
        pass

    def dispatch(self, id: Union[str, None] = None, data: dict = {}) -> None:
        """[summary]

        Args:
            id (Union[str, None], optional): [description]. Defaults to None.
            data (dict, optional): [description]. Defaults to {}.

        Raises:
            CompanyEventExcepion: [description]

        Returns:
            [type]: [description]
        """
        try:
            logger.info(f'start loop event {self.__event}')
            send_loop = asyncio.new_event_loop()
            t = Thread(target=run, args=(send_loop, self.__event, self.__eventMapping, id, data))
            t.start()
        except Exception as e:
            logger.error({"error": f"company dispatch {self.__event} : {e.__repr__}"})
            logger.error(traceback.format_exc())
            raise CompanyEventExcepion(e)
        return None


def run(loop, eventName: str, eventMapping: dict, id: Union[str, None], data: dict):
    """[summary]

    Args:
        loop ([type]): [description]
        eventName (str): [description]
        eventMapping (dict): [description]
        id (Union[str, None]): [description]
        data (dict): [description]
    """
    asyncio.set_event_loop(loop)
    eventMapping[eventName]().run(id=id, data=data)
    loop.close()
