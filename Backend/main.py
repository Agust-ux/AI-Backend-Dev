from fastapi import FastAPI
from database import engine, Base
from models import AILog

# Lag FastAPI-objektet
app = FastAPI()

# Opprett tabellen i databasen
Base.metadata.create_all(bind=engine)
print("Tabellene er laget!")

# Test endpoint
@app.get("/")
def read_root():
    return {"message": "Hei, verden!"}
