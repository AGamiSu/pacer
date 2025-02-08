from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
import config

Base = declarative_base()
engine = create_engine(config.DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

class UserSteps(Base):
    __tablename__ = "user_steps"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True)
    steps = Column(Integer, default=0)

def init_db():
    Base.metadata.create_all(engine)