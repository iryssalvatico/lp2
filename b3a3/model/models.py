from decimal import Decimal
from sqlalchemy import Column, Integer, String, Date, Sequence, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import DECIMAL, VARCHAR, DateTime

Base = declarative_base()


class Cliente(Base):
    
    _tablename_ = 'b3a3_cliente'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True, autoincrement=0, nullable=False)
    endereco = (Column(VARCHAR(255)))
    CPF = Column(Integer)
    livros_pegos = Column(VARCHAR(255))
    dia = Column(Date)
    def _repr_(self):
        return f'Cliente {self.nome}'



class Livro(Base):
    _tablename_ = 'b3a3_Livraria'
    id = Column(Integer, Sequence('publica_id_seq'), primary_key=True, autoincrement=0,nullable=False)
    autor = Column(String(40))
    editora_id = Column(Integer)
    assunto = Column(String(70))
    ISBN = Column(VARCHAR(255))
    quantidade = Column(Integer)
    def _repr_(self):
        return f'Livro {self.descricao}'

class Livraria(Base):
    _tablename_ = 'b3a3_Livraria'
    id = Column(Integer, Sequence('publica_id_seq'), primary_key=True, autoincrement=0,nullable=False)
    livro_id = Column(Integer)
    editora_id = Column(Integer)
    def _repr_(self):
        return f'Livraria {self.descricao}'



class Editora(Base):
    _tablename_ = 'b3a3_Editora'
    id = Column(Integer,primary_key=True,nullable=False)
    endereco = Column(VARCHAR(255))
    telefone = Column(Integer)
    gerente =  Column(String(40))
    def _repr_(self):
        return f'Editora {self.descricao}'