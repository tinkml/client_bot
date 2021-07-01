from pydantic import BaseModel as PydanticModel


class BaseModel(PydanticModel):
    class Config:
        orm_mode = True
