from curses import meta
import string
from sqlalchemy import Table, Column
from config.db import meta, engine
from sqlalchemy.sql.sqltypes import Integer, String

stadiums = Table("Stadiums", meta, 
    Column("id",Integer, primary_key = True),
    Column("name",String(255)),
    Column("capacity",Integer),
    Column("image",String(255))
)

meta.create_all(engine)