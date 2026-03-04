import yfinance as yf
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.db.database import SessionLocal
from app.models.symbol import Symbol
from app.models.price import Price


def fetch_latest_price(ticker: str):
    ticker_data = yf.Ticker(ticker)
    data = ticker_data.history(period="1d", interval="1m")

    if data.empty:
        return None

    latest_row = data.iloc[-1]

    return {
        "price": float(latest_row["Close"]),
        "volume": float(latest_row["Volume"]),
    }


def ingest_symbol(db: Session, symbol: Symbol):
    market_data = fetch_latest_price(symbol.ticker)

    if not market_data:
        return

    price = Price(
        symbol_id=symbol.id,
        price=market_data["price"],
        volume=market_data["volume"],
    )

    db.add(price)
    db.commit()


def run_ingestion():
    db = SessionLocal()

    try:
        symbols = db.execute(select(Symbol)).scalars().all()

        for symbol in symbols:
            print(f"Ingesting {symbol.ticker}")
            ingest_symbol(db, symbol)

    finally:
        db.close()


if __name__ == "__main__":
    run_ingestion()