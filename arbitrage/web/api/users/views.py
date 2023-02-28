from fastapi import APIRouter

from arbitrage.db.models.users import User
from arbitrage.web.api.users.schema import CreateUserSchema

router = APIRouter()


# Create user
@router.post("/")
async def create_user(body: CreateUserSchema) -> int:
    new_user = await User.create(name=body.name, external_id=body.external_id)
    return new_user.id


# Get user total deals
# @router.get("/{user_id}/deals", response_model=UserDealsSchema)
# async def get_user_deals(user_id: int) -> UserDealsSchema:
#     user = await User.filter(id=user_id).first()
#     if not user:
#         raise HTTPException(status_code=404, detail=f"User {user_id} not found")
#     deals = await user.deals()
#     return UserDealsSchema(deal_list=deals)
