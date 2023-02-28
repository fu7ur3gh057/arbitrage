from tortoise import Model, fields


class ChatRoom(Model):
    id = fields.IntField(pk=True)
    customer_id = fields.IntField()
    performer_id = fields.IntField()
    created = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "chat_rooms"


class ChatMessage(Model):
    id = fields.IntField(pk=True)
    room = fields.ForeignKeyField("models.ChatRoom", related_name="messages")
    sender = fields.ForeignKeyField("models.User", related_name="messages")
    text = fields.TextField()
    created = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "chat_messages"
