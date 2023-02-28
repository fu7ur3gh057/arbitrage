from enum import Enum

from tortoise import Model, fields

from arbitrage.db.models.payments import Currency


class DealType(str, Enum):
    REGULAR = "regular"


class DealStatus(str, Enum):
    CREATED = "Created"
    DENY_PERFORMER = "DenyPerformer"
    IN_PROCESS = "InProcess"
    CLOSE = "Close"
    ARB_CLOSE_CUSTOMER = "ArbCloseCustomer"
    ARB_CLOSE_PERFORMER = "ArbClosePerfomer"


class Deal(Model):
    id = fields.IntField(pk=True)
    customer = fields.ForeignKeyField("models.User", related_name="customer_deals")
    performer = fields.ForeignKeyField("models.User", related_name="performer_deals")
    title = fields.CharField(max_length=255)
    description = fields.TextField()
    price = fields.FloatField()
    currency = fields.CharEnumField(enum_type=Currency)
    deadline = fields.DatetimeField(null=True)
    type = fields.CharEnumField(enum_type=DealType)
    status = fields.CharEnumField(DealStatus)
    room = fields.ForeignKeyField("models.ChatRoom", related_name="deal", null=True)
    created = fields.DatetimeField(auto_now_add=True)
    updated = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "deals"
