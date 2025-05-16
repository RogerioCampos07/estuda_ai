from db import engine, create_db_and_tables
from datetime import date, datetime, time

from sqlmodel import Session
from models import Curso, Aula

create_db_and_tables(engine)

def create_curso(curso: Curso):
    """Create a new curso."""
    with Session(engine) as session:
        session.add(curso)
        session.commit()
        session.refresh(curso)
    return curso

def create_aula(aula: Aula):
    """Create a new aula."""
    with Session(engine) as session:
        session.add(aula)
        session.commit()
        session.refresh(aula)
    return aula

def get_curso(curso_id: int):
    """Get a curso by id."""
    with Session(engine) as session:
        curso = session.get(Curso, curso_id)
    return curso

def get_aula(aula_id: int):
    """Get a aula by id."""
    with Session(engine) as session:
        aula = session.get(Aula, aula_id)
    return aula


portugues = Curso(
    nome='Curso de Português',
    ativo=True,
    data_criacao=date.today(),
    data_atualizacao=date.today(),
    total_horas=time(1,0,0)
)

create_curso(portugues)

