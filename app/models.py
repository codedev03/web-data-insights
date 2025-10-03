from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
Base = declarative_base()

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    url = Column(String)
    author = Column(String)
    score = Column(Integer)
    scraped_at = Column(DateTime, default=datetime.utcnow)

# Database setup
engine = create_engine("sqlite:///data.db")  # or your preferred DB URL
Session = sessionmaker(bind=engine)
session = Session()
