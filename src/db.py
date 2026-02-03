import os # Leer Variables de Entorno
from dotenv import load_dotenv # Carga archivo .env
from sqlalchemy import create_engine # Crea una conexión reutilizable

load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")
DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    raise ValueError("DATABASE_URL no está definida")


engine = create_engine(DATABASE_URL)