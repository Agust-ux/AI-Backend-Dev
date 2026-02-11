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