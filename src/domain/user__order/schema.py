from decimal import Decimal
from pydantic import BaseModel

class UserOrderSchema(BaseModel):
    id : int
    user_id: int
    order_id: int