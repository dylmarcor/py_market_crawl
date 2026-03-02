from sqlalchemy import Session
from sqlalchemy.orm import select
from app.models.symbol import Symbol

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

def list_symbols(db: Session) -> list[Symbol]:
    return list(db.execute(select(Symbol).order_by(Symbol.ticker)).scalars().all())

def get_symbol(db: Session, ticker: str) -> Symbol | None:
    ticker = ticker.upper().strip()
    return db.execute(select(Symbol).where(Symbol.ticker == ticker)).scalar_one_or_none()