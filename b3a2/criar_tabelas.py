from sqlalchemy import *

from model.models import Usuario, Atividade, Curtida, Comentario_lp2

engine = create_engine("mysql+pymysql://primeiro_20202017238:cefetMG20202017238@primeiro.cefetvga.pro.br/primeiro_20202017238?charset=utf8mb4")

Usuario._table_.create(engine, checkfirst=True)
Atividade._table_.create(engine, checkfirst=True)
Curtida._table_.create(engine, checkfirst=True)
Comentario_lp2._table_.create(engine, checkfirst=True)