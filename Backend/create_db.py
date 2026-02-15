from database import engine, Base
from models import AILog

Base.metadata.create_all(bind=engine)
print("Tabellene er laget!")
