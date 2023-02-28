from fastapi.routing import APIRouter

from arbitrage.web.api import chat, deals, payments, users

api_router = APIRouter()
api_router.include_router(users.router, prefix="/user")
api_router.include_router(deals.router, prefix="/deals")
api_router.include_router(chat.router, prefix="/chat")
api_router.include_router(payments.router, prefix="/payments")
