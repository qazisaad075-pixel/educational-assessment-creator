from sqlalchemy import create_engine, Column, Integer, String, JSON, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime

# ⚠️ IMPORTANT: Supabase PostgreSQL connection
DATABASE_URL = "postgresql://postgres:Qazi03071119195@db.ntddhsbltawtgdvhnetq.supabase.co:5432/postgres"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


# =========================
# DATABASE MODEL (UPDATED)
# =========================
class Assessment(Base):
    __tablename__ = "assessments"

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String)
    grade_level = Column(Integer)
    topic = Column(String)

    objectives = Column(JSON)
    questions = Column(JSON)
    rubrics = Column(JSON)
    analytics = Column(JSON)

    # 🔥 NEW: shareable link system
    share_id = Column(String, unique=True, index=True)

    created_at = Column(DateTime, default=datetime.utcnow)


# =========================
# CREATE TABLES
# =========================
def create_tables():
    Base.metadata.create_all(bind=engine)


# =========================
# DB SESSION
# =========================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()