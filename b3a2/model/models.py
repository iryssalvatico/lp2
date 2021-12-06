from decimal import Decimal
from sqlalchemy import Column, Integer, String, Date, Sequence, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import DECIMAL, VARCHAR, DateTime

Base = declarative_base()


class Usuario(Base):
    
    _tablename_ = 'b3a2_usuario'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True, autoincrement=0, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    senha = Column(String(45), nullable=False)

    def _repr_(self):
        return f'Usuario {self.nome}'

    @classmethod
    def find_by_email(cls, session, email):
        return session.query(cls).filter_by(email=email).one()



class Atividade(Base):
    _tablename_ = 'b3a2_atividade'
    id = Column(Integer, Sequence('publica_id_seq'), primary_key=True, autoincrement=0,nullable=False)
    inicio = Column(DateTime)
    fim = Column(DateTime)
    quilometros = Column(Decimal (10,2))
    tipo_atividade =Column(VARCHAR(45))
    local =Column(VARCHAR(255))
    usuario_id = Column(Integer,nullable=False)

    def _repr_(self):
        return f'Atividade {self.descricao}'


class Curtida(Base):
    _tablename_ = 'b3a2_curtida'
    usuario_id = Column(Integer,primary_key=True,nullable=False)
    atividade_id = Column(Integer,primary_key=True,nullable=False)
    def _repr_(self):
        return f'Curtida {self.descricao}'

class Comentario_lp2(Base):
    _tablename_ = 'b3a2_comentario_lp2'
    id = Column(Integer, Sequence('publica_id_seq'), primary_key=True, autoincrement=0,nullable=False)
    comentario = Column(VARCHAR(255))
    usuario_id = Column(Integer,nullable=False)
    atividade_id = Column(Integer,nullable=False)
    def _repr_(self):
        return f'Comentario_lp2 {self.descricao}'