from fastapi import FastAPI
from database import SessionLocal, engine, Base
from models import AILog
from ai_service import ask_ai
#logging
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Lag FastAPI-objektet
app = FastAPI()

# Opprett tabellen i databasen
Base.metadata.create_all(bind=engine)

# # Test endpoint
# @app.get("/")
# def read_root():
#     return {"message": "Hello world!"}

@app.post("/ask")
def ask_question(prompt: str):
    start_time = time.time()

    try:
        logger.info(f"New request received: {prompt.prompt}")

        ai_response = ask_ai(prompt.prompt)

        db = SessionLocal()
        new_log = AILog(
            prompt=prompt.prompt,
            response=ai_response["answer"],
            tokens=ai_response["tokens"]
        )
        db.add(new_log)
        db.commit()
        db.close()

        duration = time.time() - start_time
        logger.info(f"Request completed in {duration:.2f} seconds")

        return ai_response

    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")
        return {"error": "Something went wrong"}