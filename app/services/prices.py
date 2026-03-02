from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.price import Price
from app.models.symbol import Symbol

def add_price(db: Session, ticker: str, price: float, volume: float | None = None) -> Price:
    ticker = ticker.upper().strip()
        
    sym = db.execute(
        select(Symbol).where(Symbol.ticker == ticker)
    ).scalar_one_or_none()

    if not sym:
        raise ValueError(f"Symbol '{ticker}' not found")
    
    price_obj = Price(
        symbol_id=sym.id,
        price=price,
        volume=volume,
    )

    db.add(price_obj)
    db.commit()
    db.refresh(price_obj)
    
    return price_obj

def list_prices_for_symbol(db: Session, ticker: str) -> list[Price]:
    ticker = ticker.upper().strip()
        
    sym = db.execute(
        select(Symbol).where(Symbol.ticker == ticker)
    ).scalar_one_or_none()

    if not sym:
        return []
    
    return list(db.execute(
        select(Price).where(Price.symbol_id == sym.id).order_by(Price.timestamp.desc())
    ).scalars().all())