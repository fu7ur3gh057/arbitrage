from fastapi import APIRouter, HTTPException

from arbitrage.db.models.chat import ChatRoom
from arbitrage.db.models.deals import Deal, DealStatus, DealType
from arbitrage.db.models.users import User
from arbitrage.web.api.deals.schema import (
    ConfirmDealSchema,
    CreateDealSchema,
    DealSchema,
    MessageSchema,
)

router = APIRouter()


# Check is deal is exists in DB
async def get_deal_or_404(deal_id):
    deal = await Deal.get(id=deal_id)
    if deal is None:
        raise HTTPException(status_code=404, detail="Deal is not found")
    else:
        return deal


# Create deal
@router.post("/")
async def create_deal(body: CreateDealSchema):
    customer = await User.filter(id=body.customer_id).first()
    performer = await User.filter(id=body.performer_id).first()
    if not customer:
        return {"msg": f"Customer {body.customer_id} not found"}
    if not performer:
        return {"msg": f"Performer {body.performer_id} not found"}
    new_deal = await Deal.create(
        customer=customer,
        performer=performer,
        title=body.title,
        description=body.description,
        price=body.price,
        currency=body.currency,
        type=DealType.REGULAR,
        status=DealStatus.CREATED,
    )
    return {"deal_id": new_deal.id, "deal_type": new_deal.type}


# Confirm deal by ID
@router.put("/{deal_id}/confirm")
async def confirm_deal(deal_id: int):
    deal = await get_deal_or_404(deal_id=deal_id)
    if deal.status != DealStatus.CREATED:
        return MessageSchema(msg="Deal already in process or closed")
    deal.status = DealStatus.IN_PROCESS
    customer = await deal.customer
    performer = await deal.performer
    chat_room = await ChatRoom.create(
        customer_id=customer.id,
        performer_id=performer.id,
    )
    deal.room = chat_room
    await deal.save()
    return ConfirmDealSchema(deal_id=deal_id, room_id=chat_room.id)


# Deny deal by ID
@router.put("/{deal_id}/deny")
async def deny_deal(deal_id: int) -> MessageSchema:
    deal = await get_deal_or_404(deal_id=deal_id)
    if deal.status != DealStatus.CREATED:
        return MessageSchema(msg="You should contact with Arbitrage system")
    deal.status = DealStatus.DENY_PERFORMER
    await deal.save()
    return MessageSchema(msg="Deal is denied")


# Get deal by ID
@router.get("/{deal_id}")
async def get_deal(deal_id: int) -> DealSchema:
    deal = await get_deal_or_404(deal_id=deal_id)
    customer = await deal.customer
    performer = await deal.performer
    room = await deal.room
    room_id = room.id if room is not None else None
    return DealSchema(
        id=deal.id,
        customer_id=customer.id,
        performer_id=performer.id,
        title=deal.title,
        description=deal.description,
        price=deal.price,
        currency=deal.currency,
        deadline=deal.deadline,
        type=deal.type,
        status=deal.status,
        room_id=room_id,
        created=deal.created,
        updated=deal.updated,
    )
