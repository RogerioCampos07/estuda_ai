from sqlmodel import Field, SQLModel
from datetime import datetime


class Curso(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nome: str
    ativo: bool = Field(default=True)
    data_criacao: str
    data_atualizacao: str
    
    
    def __repr__(self):
        return f"Curso {self.nome}"
   
class Diciplina(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nome: str
    ativo: bool = Field(default=True)
    data_criacao: str
    data_atualizacao: str
    
    def __repr__(self):
        return f"Materia {self.nome}"
    
class EstudoDiario(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    data: str
    inicio: datetime
    fim:datetime
    total_horas: str
    
    def __repr__(self):
        return f"Estudo Diario {self.data}"