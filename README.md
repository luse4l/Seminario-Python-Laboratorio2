Comandos terminal
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt


explicaciones:
database.py Habla con SQLite. Define cómo se estructuran y guardan las tablas en tu disco duro.

schema.py Habla con el cliente (un navegador, el frontend, Postman). Valida qué datos te pueden enviar al crear algo (POST) y le da formato JSON a lo que vos les devolvés (GET).

