from sqlmodel import create_engine, SQLModel


sql_url = "sqlite:///./database.db"
engine = create_engine(sql_url, echo=True)


def create_db_and_tables(engine):
    """Create the database and tables."""
    SQLModel.metadata.create_all(engine)
