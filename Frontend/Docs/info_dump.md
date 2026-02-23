# Hva var det igjen?

---
venv
---
venv står for virtual environment (virtuelt miljø).
Det er en isolert mini-Python på din PC som bare dette prosjektet bruker.

Uten venv:
- Alle prosjekter deler samme Python
- Alle pakker installeres globalt
- Versjoner kan krasje
- Ett prosjekt kan ødelegge et annet

Med venv:
- Hvert prosjekt får sitt eget miljø
- Egne pakker
- Egne versjoner
- Null konflikt

*Hva ligger egentlig i venv-mappen?*

Inni venv/ ligger:
- En kopi av Python
- Alle pakkene du installerer
- Intern struktur som gjør at miljøet er isolert
- Du skal aldri redigere noe inni venv manuelt.

---
SQLite
---
SQLite er en type SQL-database.
    Men i stedet for at databasen kjører på en egen server,
    er hele databasen bare én fil på PC-en. **ai_logs.db**

- Krever ingen server
- Ingen installasjon (følger med Python)
- Lager bare en .db-fil
- Perfekt for skoleprosjekter og testing