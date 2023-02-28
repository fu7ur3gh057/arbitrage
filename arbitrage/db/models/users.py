from tortoise import Model, fields


class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    external_id = fields.IntField(null=True)
    is_arbitrage = fields.BooleanField(default=False)
    created = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "users"

    async def deals(self):
        return await self.customer_deals + await self.performer_deals

    def __str__(self):
        return f"{self.id}"
