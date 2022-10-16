from fastapi import APIRouter, Response, status
from config.db import conn
from models.stadium import stadiums
from schemas.stadium import Stadium
from starlette.status import HTTP_204_NO_CONTENT


stadium = APIRouter()

@stadium.get("/stadiums", response_model=list[Stadium], tags = ["stadium"])
def getStadium():
    return conn.execute(stadiums.select()).fetchall()

@stadium.get("/stadium/{id}", response_model = Stadium, tags = ["stadium"])
def getStadium(id:int):
    return conn.execute(stadiums.select().where(stadiums.c.id == id)).first()

@stadium.post("/stadium", response_model = Stadium, tags = ["stadium"])
def createStadium(stadium: Stadium):#Stadium create in schemas
    new_Stadium = {"name": stadium.name, "capacity":stadium.capacity,"image":stadium.image}
    result = conn.execute(stadiums.insert().values(new_Stadium))
    print(result)
    return conn.execute(stadiums.select().where(stadiums.c.id == result.lastrowid)).first()

@stadium.put("/stadium/{id}", response_model = Stadium, tags = ["stadium"])
def updateStadium(id: int, stadium: Stadium):
    conn.execute(stadiums.update().values(name = stadium.name, 
    capacity = stadium.capacity,
    image = stadium.image).where(stadiums.c.id == id))
    return conn.execute(stadiums.select().where(stadiums.c.id == id)).first()


@stadium.delete("/stadium/{id}", status_code = HTTP_204_NO_CONTENT, tags = ["stadium"])
def deleteStadium(id:int):
    result = conn.execute(stadiums.delete().where(stadiums.c.id == id ))
    return Response(status_code = HTTP_204_NO_CONTENT)

