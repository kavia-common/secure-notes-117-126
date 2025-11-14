import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from dotenv import load_dotenv
load_dotenv()

# PUBLIC_INTERFACE
DATABASE_URL = os.environ.get("POSTGRES_URL") or os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("POSTGRES_URL or DATABASE_URL environment variable must be set for the backend.")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# All models should inherit from Base
Base = declarative_base()

# PUBLIC_INTERFACE
def create_db_and_tables():
    """Create all database tables if not present."""
    # Import models to register them with Base before creating tables
    from app import models  # noqa: F401
    Base.metadata.create_all(bind=engine)
