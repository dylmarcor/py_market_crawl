from sqlalchemy import select 
from sqlalchemy.orm import Session 
from app.models.symbol import Symbol
from typing import List, Optional

def add_symbol(db: Session, ticker: str) -> Symbol:
    ticker = ticker.upper().strip()
    
    existing = db.execute(select(Symbol).where(Symbol.ticker == ticker)).scalar_one_or_none()
    if existing:
        return existing
    sym = Symbol(ticker=ticker)
    db.add(sym)
    db.commit()
    db.refresh(sym)
    return sym

def list_symbols(db: Session) -> List[Symbol]:
    return list(db.execute(select(Symbol).order_by(Symbol.ticker)).scalars().all())

def get_symbol(db: Session, ticker: str) -> Optional[Symbol]:
    ticker = ticker.upper().strip()
    return db.execute(select(Symbol).where(Symbol.ticker == ticker)).scalar_one_or_none()