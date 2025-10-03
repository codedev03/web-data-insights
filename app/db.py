from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Create engine
engine = create_engine(os.getenv("DATABASE_URL"), echo=True)

# Create session factory
SessionLocal = sessionmaker(bind=engine)
