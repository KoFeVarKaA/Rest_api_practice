from pydantic import BaseModel

class UserSchema(BaseModel):
    id : int
    first_name : str
    last_name : str
    age : int
    profession_id : int | None