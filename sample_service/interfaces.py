from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from sample_service.types import Security


class ISecurityRepository(ABC):
    @abstractmethod
    def get_security(self, id: UUID) -> Security:
        pass

    @abstractmethod
    def get_securities_for_corporation(self, corporation_id: UUID) -> List[Security]:
        pass
