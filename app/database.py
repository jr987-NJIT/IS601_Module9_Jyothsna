# app/database.py

from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
import os

# Get database URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/fastapi_db")

# Database availability flag
DB_ENABLED = os.getenv("DB_ENABLED", "true").lower() == "true"

# Create SQLAlchemy engine only if database is enabled
if DB_ENABLED:
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
else:
    engine = None
    SessionLocal = None

# Base class for models
Base = declarative_base()

# User model
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationship to calculations
    calculations = relationship("Calculation", back_populates="user", cascade="all, delete-orphan")

# Calculation model
class Calculation(Base):
    __tablename__ = "calculations"
    
    id = Column(Integer, primary_key=True, index=True)
    operation = Column(String(20), nullable=False)
    operand_a = Column(Float, nullable=False)
    operand_b = Column(Float, nullable=False)
    result = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    
    # Relationship to user
    user = relationship("User", back_populates="calculations")

# Function to get database session
def get_db():
    if not DB_ENABLED or SessionLocal is None:
        yield None
        return
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Function to initialize database
def init_db():
    if DB_ENABLED and engine is not None:
        Base.metadata.create_all(bind=engine)
