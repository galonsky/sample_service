from decimal import Decimal
from uuid import UUID

from sample_service.interfaces import ISecurityRepository
from sample_service.types import Security


class SecurityService:
    def __init__(self, security_repository: ISecurityRepository):
        self.repository = security_repository

    def get_security(self, id: UUID) -> Security:
        return self.repository.get_security(id)

    def change_quantity(self, id: UUID, new_quantity: Decimal):
        security = self.get_security(id)
        # change quantity
