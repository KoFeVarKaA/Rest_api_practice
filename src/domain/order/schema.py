from decimal import Decimal
from pydantic import BaseModel

class OrderSchema(BaseModel):
    id : int
    name: str
    total_sum: Decimal