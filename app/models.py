from enum import Enum

from tortoise import fields
from tortoise.models import Model


class CommodityType(str, Enum):
    room = "room"
    studio = "studio"
    house = "house"


class Commodity(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    kind = fields.CharEnumField(CommodityType)
    price_per_night = fields.DecimalField(8, 2)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.data
