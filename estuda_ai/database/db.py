from sqlmodel import create_engine, SQLModel
from dotenv import load_dotenv
import os

load_dotenv()

sql_url = os.getenv('DATABASE_URL')
engine = create_engine(sql_url)


def create_db_and_tables(engine):
    """Create the database and tables."""
    SQLModel.metadata.create_all(engine)






