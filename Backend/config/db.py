#Utilizamos sqlalchemy que es un orm para python

from sqlalchemy import create_engine, MetaData


# Esto necesita conectarse a un url, en este caso utilizamos pymysql
engine = create_engine("mysql+pymysql://root:123456789@localhost:3306/futbol")

meta = MetaData()

conn = engine.connect()