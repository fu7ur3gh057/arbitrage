from typing import List, Optional

from pydantic import BaseModel

from arbitrage.web.api.deals.schema import DealSchema


class CreateUserSchema(BaseModel):
    name: str
    external_id: Optional[int] = None


class UserDealsSchema(BaseModel):
    deal_list = List[DealSchema]

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True
