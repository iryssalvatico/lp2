from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from model.models import Usuario, Atividade, Comentario_lp2, Curtida, Curtida_comentario

engine = create_engine("mysql+pymysql://primeiro_20202017238:cefetMG20202017238@primeiro.cefetvga.pro.br/primeiro_20202017238?charset=utf8mb4", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

def create():

    user1 = Usuario(email='fefepaiva@gmail.com', senha='123', nome='Fernanda Paiva.', data_nascimento='2000-04-10')
    session.add(user1) 
    user2 = Usuario(email='malucosta@gmail.com', senha='456', nome='Maria Luisa Costa.', data_nascimento='2001-02-09')
    session.add(user2)
    user3 = Usuario(email='jujuasis@gemail.com', senha='789', nome='Julia Assis.', data_nascimento='2002-07-01')
    session.add(user3)


    atividade1 = Atividade( descricao_atividade = 'Estudando para o vestibular.', usuario_id = '1')
    session.add(atividade1)
    atividade2 = Atividade( descricao_atividade = 'Viagem para Mykonos.', usuario_id = '2')
    session.add(atividade2)
    atividade3 = Atividade( descricao_atividade = 'Festa com amigos.', usuario_id = '3')
    session.add(atividade3)


    curtida1 = Curtida( usuario_id = '1', atividade_id = '2')
    session.add(curtida1)
    curtida2 = Curtida( usuario_id = '2', atividade_id = '3')
    session.add(curtida2)
    curtida3 = Curtida( usuario_id = '3', atividade_id = '1')
    session.add(curtida3)


    comentario1 = Comentario_lp2( comentario = 'Você se esforça e estuda muito, essa vaga já é sua!!', usuario_id ='3', atividade_id ='1')
    session.add(comentario1)
    comentario2 = Comentario_lp2( comentario = 'Grécia e suas maravilhas!', usuario_id ='1', atividade_id ='2')
    session.add(comentario2)
    comentario3 = Comentario_lp2( comentario = 'Saudades de vcs!', usuario_id ='2', atividade_id ='3')
    session.add(comentario3)


    curtida_comentario1 = Curtida_comentario( usuario_id ='1', comentario_lp2_id ='1')
    session.add(curtida_comentario1)
    curtida_comentario2 = Curtida_comentario( usuario_id ='2', comentario_lp2_id ='2')
    session.add(curtida_comentario2)
    curtida_comentario3 = Curtida_comentario( usuario_id ='3', comentario_lp2_id ='3')
    session.add(curtida_comentario3)

    session.commit()



create()