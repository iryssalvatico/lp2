from sqlalchemy import *
from model.models import Cliente, Editora, Livraria, Livro


engine = create_engine("mysql+pymysql://primeiro_20202017238:cefetMG20202017238@primeiro.cefetvga.pro.br/primeiro_20202017238?charset=utf8mb4")

Cliente._table_.create(engine, checkfirst=True)
Livraria._table_.create(engine, checkfirst=True)
Editora._table_.create(engine, checkfirst=True)
Livro._table_.create(engine, checkfirst=True)