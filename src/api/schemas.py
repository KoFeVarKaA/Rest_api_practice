from pydantic import BaseModel

class ResponseSchema(BaseModel):
     code : int
     message: str