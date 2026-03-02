from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.services.psql_utc import utcnow

from app.db.base import Base

class Price(Base):
    __tablename__ = "prices"

    id = Column(Integer, primary_key=True, index=True)

    symbol_id = Column(Integer, ForeignKey("symbols.id"), nullable=False)

    timestamp = Column(
        DateTime(timezone=True),
        server_default=utcnow(),
        index=True
    )
    price = Column(Float, nullable=False)
    volume = Column(Float, nullable=True)
    
    symbol = relationship("Symbol", backref="prices")