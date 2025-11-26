from sqlalchemy import Column, String, DateTime
from database import Base

class Polymer(Base):
    __tablename__ = "polymers"

    timestamp = Column(DateTime, primary_key=True)
    polymer = Column(String(128), nullable=False)
