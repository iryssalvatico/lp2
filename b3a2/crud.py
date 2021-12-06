from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from model.models import Usuario, Atividade, Comentario_lp2, Curtida

engine = create_engine("mysql+pymysql://primeiro_20202017238:cefetMG20202017238@primeiro.cefetvga.pro.br/primeiro_20202017238?charset=utf8mb4", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

def create():

    usuario1 = Usuario(id='1',email='usu1@usu.com',senha='usuario123')
    usuario2 = Usuario(id='2',email='usu2@usu.com',senha='usuario123')
    usuario3 = Usuario(id='3',email='usu3@usu.com',senha='usuario123') 
    session.add(usuario1)
    session.add(usuario2)
    session.add(usuario3)


    atividade1 = Atividade(
        id='1',
        inicio='2021-06-11 14:28:30',
        fim='2021-06-11 12:30:20',
        quilometros='10',
        tipo_atividade='Caminhada',
        local='VGA',
        usuario_id='1')


    atividade2 = Atividade(
        id='2',
        inicio='2021-02-16 08:30:16',
        fim='2021-02-16 09:15:27',
        quilometros='12',
        tipo_atividade='Natação',
        local='VGA',
        usuario_id='1')

    atividade3 = Atividade(
        id='3',
        inicio='2021-04-17 09:09:09',
        fim='2021-04-17 10:10:10',
        quilometros='15',
        tipo_atividade='Maratona',
        local='-',
        usuario_id='1')

    atividade4 = Atividade(
        id='4',
        inicio='2021-03-21 12:00:00',
        fim='2021-03-21 13:00:00',
        quilometros='10',
        tipo_atividade='Maratona aquática',
        local='VGA',
        usuario_id='2')

    atividade5 = Atividade(
        id='5',
        inicio='2021-09-12 12:30:12',
        fim='2021-09-12 13:30:19',
        quilometros='20',
        tipo_atividade='Canoagem',
        local='VGA',
        usuario_id='2')

    atividade6 = Atividade(
        id='6',
        inicio='2021-07-12 17:30:12',
        fim='2021-07-12 18:40:12',
        quilometros='23',
        tipo_atividade='Remo',
        local='-',
        usuario_id='2')

    atividade7 = Atividade(
        id='7',
        inicio='2021-10-09 11:00:12',
        fim='2021-10-09 12:01:09',
        quilometros='15',
        tipo_atividade='Skate',
        local='VGA',
        usuario_id='3')

    atividade8 = Atividade(
        id='8',
        inicio='2021-08-09 20:00:12',
        fim='2021-08-09 21:00:34',
        quilometros='10',
        tipo_atividade='Patinação',
        local='VGA',
        usuario_id='3')

    atividade9 = Atividade(
        id='9',
        inicio='2021-08-02 14:08:23',
        fim='2021-08-02 16:09: 21',
        quilometros='68',
        tipo_atividade='Motociclismo',
        local='-',
        usuario_id='3')

    session.add(atividade1)
    session.add(atividade2)
    session.add(atividade3)
    session.add(atividade4)
    session.add(atividade5)
    session.add(atividade6)
    session.add(atividade7)
    session.add(atividade8)
    session.add(atividade9)

    comentario1 = Comentario_lp2(usuario_id='2', atividade_id='1', id='1',comentario='Que caminhada leve! Nada melhor para a saúde!')
    comentario2 = Comentario_lp2(usuario_id='3', atividade_id='4', id='2',comentario='Tem que ter fôlego!')
    comentario3 = Comentario_lp2(usuario_id='1', atividade_id='8', id='3',comentario='Que lindo, que leveza, tem que ser experiente!')
    comentario4 = Comentario_lp2(usuario_id='2', atividade_id='9', id='4',comentario='Cuidado em, você não é o motoqueiro fantasma! ')
    session.add(comentario1)
    session.add(comentario2)
    session.add(comentario3)
    session.add(comentario4)

    curtida1 = Curtida(usuario_id='1',atividade_id='2')
    curtida2 = Curtida(usuario_id='1',atividade_id='3')
    curtida3 = Curtida(usuario_id='1',atividade_id='4')
    curtida4 = Curtida(usuario_id='1',atividade_id='5')
    curtida5 = Curtida(usuario_id='1',atividade_id='6')
    curtida6 = Curtida(usuario_id='1',atividade_id='7')
    curtida7 = Curtida(usuario_id='2',atividade_id='1')
    curtida8 = Curtida(usuario_id='2',atividade_id='3')
    curtida9 = Curtida(usuario_id='2',atividade_id='4')
    curtida10 = Curtida(usuario_id='2',atividade_id='5')
    curtida11 = Curtida(usuario_id='2',atividade_id='8')
    curtida12 = Curtida(usuario_id='2',atividade_id='9')
    curtida13 = Curtida(usuario_id='3',atividade_id='1')
    curtida14 = Curtida(usuario_id='3',atividade_id='2')
    curtida15 = Curtida(usuario_id='3',atividade_id='6')
    curtida16 = Curtida(usuario_id='3',atividade_id='7')
    curtida17 = Curtida(usuario_id='3',atividade_id='8')
    curtida18 = Curtida(usuario_id='3',atividade_id='9')

    session.add(curtida1)
    session.add(curtida2)
    session.add(curtida3)
    session.add(curtida4)
    session.add(curtida5)
    session.add(curtida6)
    session.add(curtida7)
    session.add(curtida8)
    session.add(curtida9)
    session.add(curtida10)
    session.add(curtida11)
    session.add(curtida12)
    session.add(curtida13)
    session.add(curtida14)
    session.add(curtida15)
    session.add(curtida16)
    session.add(curtida17)
    session.add(curtida18)

    session.commit()
create()