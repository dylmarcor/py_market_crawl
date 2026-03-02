from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.api.schemas import SymbolCreate, SymbolOut
from app.services.symbols import add_symbol, list_symbols, get_symbol

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok"}

@router.post("/symbols", response_model=SymbolOut)
def create_symbol(payload: SymbolCreate, db: Session = Depends(get_db)):
    sym = add_symbol(db, payload.ticker)
    return sym

@router.get("/symbols", response_model=list[SymbolOut])
def read_symbol(db: Session = Depends(get_db)):
    return list_symbols(db)

@router.get("/symbols/{ticker}", response_model=SymbolOut)
def read_symbol(ticker: str, db: Session = Depends(get_db)):
    sym = get_symbol(db, ticker)
    if not sym:
        raise HTTPException(status_code=404, detail="Symbol not found")
    return sym