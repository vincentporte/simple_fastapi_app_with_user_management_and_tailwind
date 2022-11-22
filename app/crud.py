from typing import List

from app.models import Commodity


async def add(name: str, kind: str, price_per_night: float) -> Commodity:
    commodity = await Commodity.create(name=name, kind=kind, price_per_night=price_per_night)
    return commodity


async def get(id: int) -> Commodity:
    commodity = await Commodity.get_or_none(id=id)
    return commodity


async def get_all() -> List[Commodity]:
    commodities = await Commodity.all()
    return commodities


async def filter_by(text: str) -> List[Commodity]:
    commodities = await Commodity.filter(name__icontains=text)
    return commodities


async def update(commodity: Commodity, commodity_data: dict):
    for field_name in commodity_data:
        setattr(commodity, field_name, commodity_data.get(field_name))
    await commodity.save()
    return commodity
