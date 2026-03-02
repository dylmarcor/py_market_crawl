from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.api.schemas import SymbolCreate, SymbolOut, PriceCreate, PriceOut
from app.db.deps import get_db
from app.services.symbols import add_symbol, list_symbols, get_symbol
from app.services.prices import add_price, list_prices_for_symbol

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok"}

# Symbol routes
@router.post("/symbols", response_model=SymbolOut)
def create_symbol(payload: SymbolCreate, db: Session = Depends(get_db)):
    try:
        sym = add_symbol(db, payload.ticker)
        return sym
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) 

@router.get("/symbols", response_model=List[SymbolOut])
def read_symbol(db: Session = Depends(get_db)):
    return list_symbols(db)

@router.get("/symbols/{ticker}", response_model=SymbolOut)
def read_symbol(ticker: str, db: Session = Depends(get_db)):
    sym = get_symbol(db, ticker)
    if not sym:
        raise HTTPException(status_code=404, detail="Symbol not found")
    return sym

# Price routes
@router.post("/prices", response_model=PriceOut)
def create_price(payload: PriceCreate, db: Session = Depends(get_db)):
    try:
        price = add_price(db, payload.ticker, payload.price, payload.volume)
        return price
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/prices/{ticker}", response_model=List[PriceOut])
def read_prices(ticker: str, db: Session = Depends(get_db)):
    return list_prices_for_symbol(db, ticker)   