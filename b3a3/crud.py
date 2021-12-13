from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from model.models import Cliente, Editora, Livraria, Livro

engine = create_engine("mysql+pymysql://primeiro_20202017238:cefetMG20202017238@primeiro.cefetvga.pro.br/primeiro_20202017238?charset=utf8mb4", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

def create():

    client1 = Cliente(id='1', endereco = 'Rua Rio Branco, nº 1', CPF = '12345678901', livros_pegos='É assim que acaba', dia ='2021-12-01' )
    session.add(client1) 
    client2 = Cliente(id='2', endereco = 'Rua Imigrantes, nº 2', CPF = '98765432100', livros_pegos='Orgulho e preconceito', dia ='2021-12-02' )
    session.add(client2)
    client3 = Cliente(id='3', endereco = 'Rua Anchieta, nº 3', CPF = '13579086427', livros_pegos='Simplesmente Acontece', dia ='2021-12-03' )
    session.add(client3)

    editora1 =Editora(id='4', endereco = 'Rua Dutra, nº 4 ', telefone= '(35)3265-1342', Gerente ='Julia Moraes')
    session.add(editora1)
    editora2 =Editora(id='5', endereco = 'Rua Ibirapuera , nº 5', telefone= '(35)3265-9832', Gerente ='Bruno Pontes')
    session.add(editora2)
    editora3 =Editora(id='6', endereco = 'Rua Borba Gato , nº 6 ', telefone= '(35)3265-7632', Gerente ='Lucas Ferreira')
    session.add(editora3)

    livraria1 = Livraria( id='7', livro_id='10', editora_id='4')
    session.add(livraria1)
    livraria2 = Livraria( id='8', livro_id='11', editora_id='5')
    session.add(livraria2)
    livraria3 = Livraria( id='9', livro_id='12', editora_id='6')
    session.add(livraria3)

    livro1 = Livro(id='10', aoutor='Coollen Hoover', editora_id='4',assunto='lovers to acquaintances and friends to lovers', ISBN ='345-65-76392-01-4', quantidade='50')
    session.add(livro1)
    livro2 = Livro(id='11', aoutor='Jane Austen', editora_id='5',assunto='enemies for lovers', ISBN ='764-65-23789-98-1', quantidade='100')
    session.add(livro2)
    livro3 = Livro(id='12', aoutor='Cecelia Ahern', editora_id='6',assunto='friends for lovers', ISBN ='267-65-98765-7', quantidade='150')
    session.add(livro3)

    session.commit()

create()