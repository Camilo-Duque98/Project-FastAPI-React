from fastapi import FastAPI
from routes.stadium import stadium

# Define API object

app = FastAPI(
    title = "Stadium API",
    openapi_tags = [{
        "name" : "stadiums",
        "description": "descriptions api of stadiums of world"
    }]
)

app.include_router(stadium)

