from datetime import date, datetime, time

from sqlmodel import Field, SQLModel


class Curso(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nome: str
    ativo: bool = Field(default=True)
    data_criacao: date
    data_atualizacao: date
    total_horas: time

    def __repr__(self):
        return f'Curso {self.nome}'


class Aula(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    curso_id: int = Field(foreign_key='curso.id')
    nome: str
    total_horas: time

    def __repr__(self):
        return f'Aula: {self.nome}'
    

class Estudo(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    curso_id: int = Field(foreign_key='curso.id')
    aula_id: int = Field(foreign_key='aula.id')
    data_estudo: datetime
    inicio: datetime
    fim: datetime
    horas_estudadas: time

    def __repr__(self):
        return f'Estudo {self.data_estudo} - {self.horas_estudadas}'
    


