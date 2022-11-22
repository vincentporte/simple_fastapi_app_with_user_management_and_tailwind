from typing import List

from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from app.crud import add, filter_by, get, get_all, update
from app.schemas import Commodity

commodity_routes = APIRouter()


@commodity_routes.get("", response_model=List[Commodity])
async def get_commodities():
    return await get_all()


@commodity_routes.post("", response_model=Commodity)
async def add_commodity(commodity: Commodity):
    return await add(name=commodity.name, kind=commodity.kind, price_per_night=commodity.price_per_night)


@commodity_routes.get("/{text}", response_model=List[Commodity])
async def filter_commodities_by_text(text: str):
    return await filter_by(text=text)


@commodity_routes.put("/{id}", response_model=Commodity)
async def update_commodity(id: int, commodity_in: Commodity):
    commodity = await get(id=id)

    if not commodity:
        raise HTTPException(400, detail="Invalid Commodity")

    return await update(commodity=commodity, commodity_data=commodity_in.dict(exclude_unset=True))
