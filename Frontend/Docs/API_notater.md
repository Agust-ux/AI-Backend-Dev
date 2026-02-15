# Hva trengs i backend?

----------------
API-endpoints
----------------

*POST /ask*
    - Sender en spørring til AI og lagrer resultatet i databasen.

Input:
    - prompt
    - user_id

Output:
    - AI-svar
    - Tokenbruk
    - Status

*GET /logs*
Henter tidligere AI-forespørsler fra databasen.

-----------------
Logging og drift
-----------------
Systemet implementerer:
    - Logging av forespørsler
    - Logging av feil
    - Feilhåndtering med try/except
    - Sikker lagring av API-nøkkel via .env
    - Lagring av tokenbruk for kostnadskontroll

Dette viser forståelse for drift og produksjonsnære løsninger.

---------
Sikkerhet
---------
API-nøkkel lagres i miljøvariabler
Ingen sensitiv informasjon hardkodes
Strukturert feilhåndtering