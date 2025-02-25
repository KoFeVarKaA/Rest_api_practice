from decimal import Decimal
from pydantic import BaseModel
from src.domain.order.model import StatusEnum

class OrderSchema(BaseModel):
    id : int
    name: str
    total_amount: Decimal
    status : StatusEnum
    description : str | None