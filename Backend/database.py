from sqlalchemy import create_engine #Lager selve koblingen til databasen.
from sqlalchemy.ext.declarative import declarative_base #Lar oss lage Python-klasser som blir til SQL-tabeller.
from sqlalchemy.orm import sessionmaker #Lager en “database-session” (må brukes når vi skal lagre data senere).

DATABASE_URL = "sqlite:///./ai_logs.db" 
# Funksjonen er:
# Bruk SQLite
# Lag en fil som heter ai_logs.db
# Lag den i samme mappe

engine = create_engine( #selve koblingen til databasen
    DATABASE_URL, connect_args={"check_same_thread": False} #nødvendig for SQLite når FastAPI kjører parallelt
)
SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
) #"åpner en samtale med databasen"

Base = declarative_base()   #Alle modeller (tabeller) må arve fra Base.

#Oppsumering:
# engine = koblingen til databasen
# SessionLocal = måten vi sender og henter data på
# Base = brukes for å lage tabeller

