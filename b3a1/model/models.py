from sqlalchemy import Column, Integer, String, Date, Sequence, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text

Base = declarative_base()


class Usuario(Base):
    _tablename_ = 'usuario'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    senha = Column(String(45), nullable=False)

    nome = Column(String(25))
    data_nascimento = Column(Date)

    def _repr_(self):
        return f'Usuario {self.nome}'

    @classmethod
    def find_by_email(cls, session, email):
        return session.query(cls).filter_by(email=email).one()

class Atividade(Base):
    _tablename_ = 'atividade'
    id = Column(Integer, Sequence('publica_id_seq'), primary_key=True)
    descricao_atividade = Column(String(255))
    usuario_id = Column(Integer, ForeignKey('usuario.id'))

    def _repr_(self):
        return f'Atividade {self.descricao}'


class Curtida(Base):
    _tablename_ = 'curtida'
    id = Column(Integer, Sequence('publica_id_seq'), primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    atividade_id = Column(Integer, ForeignKey('atividade.id'))
    def _repr_(self):
        return f'Curtida {self.descricao}'

class Comentario_lp2(Base):
    _tablename_ = 'comentario_lp2'
    id = Column(Integer, Sequence('publica_id_seq'), primary_key=True)
    comentario = Column(String(255))
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    atividade_id = Column(Integer, ForeignKey('atividade.id'))
    def _repr_(self):
        return f'Comentario_lp2 {self.descricao}'


class Curtida_comentario(Base):
    _tablename_ = 'curtida_comentario'
    id = Column(Integer, Sequence('publica_id_seq'), primary_key=True)
    
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    comentario_lp2_id = Column(Integer, ForeignKey('comentario_lp2.id'))
    def _repr_(self):
        return f'Curtida_comentario {self.descricao}'