from datetime import date, datetime

from sqlmodel import Field, SQLModel


class Curso(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nome: str
    ativo: bool = Field(default=True)
    data_criacao: str
    data_atualizacao: str
    total_horas: str

    def __repr__(self):
        return f'Curso {self.nome}'


class Aula(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    curso_id: int = Field(foreign_key='curso.id')
    nome: str
    data_inicio: date
    data_fim: date
    data: date
    inicio: datetime
    fim: datetime
    total_horas: str

    def __repr__(self):
        return f'Aula: {self.nome}'
