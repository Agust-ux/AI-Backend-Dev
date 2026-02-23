from fastapi import FastAPI
from database import engine, Base
from models import AILog

# Lag FastAPI-objektet
app = FastAPI()

# Opprett tabellen i databasen
Base.metadata.create_all(bind=engine)
print("Tabellene er laget!")
# Se på alle klasser som arver fra Base
# Lag tabeller i databasen hvis de ikke finnes

# Test endpoint
@app.get("/")
def read_root():
    return {"message": "Hello world!"}
