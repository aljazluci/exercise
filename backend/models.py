from pydantic import BaseModel

class User(BaseModel):
    firstName: str | None = None
    lastName: str | None = None
    age: int | None = None
    email: str | None = None
    gender: str | None = None
    email: str | None = None
    phone: str | None = None