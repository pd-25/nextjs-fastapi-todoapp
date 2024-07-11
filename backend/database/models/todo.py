from sqlalchemy import Column, Integer, Text, Boolean, DateTime
from database.base_class import Base
from datetime import datetime
from sqlalchemy.sql import func

class Todo(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(Text, nullable=False)
    is_complete = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=func.now())