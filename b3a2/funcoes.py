from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from model.models import Usuario, Atividade
from sqlalchemy.sql.expression import desc

engine = create_engine("mysql+pymysql://primeiro_20202017238:cefetMG20202017238@primeiro.cefetvga.pro.br/primeiro_20202017238?charset=utf8mb4", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

def selecionar():

    for usuario_id, quilometros, inicio, fim in session.query(Atividade.usuario_id,Atividade.quilometros, Atividade.inicio, Atividade.fim).filter(Atividade.local=='VGA').order_by(desc(Atividade.quilometros)):
        print(usuario_id,'-',quilometros,'-',inicio,'-',fim)

def atualizar():
    user = session.query(Usuario).filter(Usuario.email=='usu1@usu.com')
    for usuario in user:
        usuario.senha = 'senhausu1'
        session.commit()

def deletar():
    for usuario_id in session.query(Usuario.id).filter(Usuario.email=='usu2@usu.com'):
        user = session.query(Usuario).get(usuario_id)
        session.delete(user)
        session.commit()

selecionar()
deletar()
atualizar()