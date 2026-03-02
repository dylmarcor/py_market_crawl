from pydantic import BaseModel, ConfigDict

class SymbolCreate(BaseModel):
    ticker: str

class SymbolOut(BaseModel):
    id: int
    ticker: str

    model_config = ConfigDict(from_attributes=True)