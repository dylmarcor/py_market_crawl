from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class SymbolCreate(BaseModel):
    ticker: str

class SymbolOut(BaseModel):
    id: int
    ticker: str

    model_config = ConfigDict(from_attributes=True)

class PriceCreate(BaseModel):
    ticker: str
    price: float
    volume: Optional[float] = None
    
class PriceOut(BaseModel):
    id: int
    price: float
    volume: Optional[float] = None
    timestamp: datetime

    model_config = ConfigDict(from_attributes=True)