from app.db.database import engine
from app.db.base import Base

# Import models so they register with SQLAlchemy metadata
from app.models.price import Price
from app.models.symbol import Symbol

def init_db():
    print("Initializing database...")
    Base.metadata.create_all(bind=engine)