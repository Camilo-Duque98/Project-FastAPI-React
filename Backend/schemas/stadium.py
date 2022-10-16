from pydantic import BaseModel
from typing import Optional

class Stadium(BaseModel):
    id: Optional[str]
    name: str
    capacity: int
    image: str