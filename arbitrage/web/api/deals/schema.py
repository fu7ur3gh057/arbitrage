from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MessageSchema(BaseModel):
    msg: str


class CreateDealSchema(BaseModel):
    customer_id: int
    performer_id: int
    title: str
    description: str
    price: float
    currency: str
    deadline: Optional[datetime] = None


class ConfirmDealSchema(BaseModel):
    deal_id: int
    room_id: int

    class Config:
        orm_mode = True


class DealSchema(BaseModel):
    id: Optional[int] = None
    customer_id: int
    performer_id: int
    title: str
    description: str
    price: float
    currency: str
    deadline: Optional[datetime] = None
    type: str
    status: str
    room_id: Optional[int] = None
    created: datetime
    updated: datetime

    class Config:
        orm_mode = True
