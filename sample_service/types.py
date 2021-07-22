import dataclasses
from decimal import Decimal
from uuid import UUID


@dataclasses.dataclass(frozen=True)
class Security:
    id: UUID
    owner_id: UUID
    corporation_id: UUID
    quantity: Decimal
