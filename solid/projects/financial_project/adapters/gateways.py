from typing import List
from core.interfaces import FinancialDataGateway
from core.entities import FinancialEntity

class FinancialDataMapper(FinancialDataGateway):
    def __init__(self):
        # Emulating the "Financial Database"
        self._db = {
            "1": FinancialEntity("1", 100.0),
            "2": FinancialEntity("2", -50.0),
            "3": FinancialEntity("3", 200.0)
        }

    def get_entities(self) -> List[FinancialEntity]:
        print("Gateway: Fetching data from Financial Database...")
        return list(self._db.values())