# Systemarkitektur

Systemet skal bygges med følgende arkitektur:

Client
↓
FastAPI Backend
↓
OpenAI API
↓
SQL Database

-----------
Forklaring
-----------
    - FastAPI håndterer HTTP-forespørsler
    - AI API genererer svar basert på prompt
    - SQL-database lagrer alle forespørsler og svar
    - Logging håndterer drift og feilhåndtering

--------------------
Teknologier i bruk
--------------------
    - Python 3
    - FastAPI
    - SQLAlchemy
    - PostgreSQL / SQLite
    - OpenAI API
    - Uvicorn

----------------
Database-design
----------------
*Tabell: ai_logs*

    - id (Primary Key)
    - user_id (String)
    - prompt (Text)
    - response (Text)
    - model_name (String)
    - tokens_used (Integer)
    - created_at (Timestamp)