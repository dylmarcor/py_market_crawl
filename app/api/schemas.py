from pydantic import BaseModel

class SymbolCreate(BaseModel):
    ticker: str

class SymbolOut(BaseModel):
    id: int
    ticker: str

    class Config:
        from_attributes: True