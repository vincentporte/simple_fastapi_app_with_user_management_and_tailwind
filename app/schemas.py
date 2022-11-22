from typing import Optional

from pydantic.main import BaseModel


class Commodity(BaseModel):
    id: Optional[int]
    name: Optional[str] = None
    kind: str
    price_per_night: float

    class Config:
        orm_mode = True
