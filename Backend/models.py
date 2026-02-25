#Her lager vi tabellen som lagrer alle spørsmål og svar fra AI:
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base

class AILog(Base):
    __tablename__ = "ai_logs"

    id = Column(Integer, primary_key=True, index=True)
    prompt = Column(String)
    response = Column(String)
    tokens = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)

# Dette lager en Python-klasse.
# Men fordi den arver fra Base, blir den en SQL-tabell.