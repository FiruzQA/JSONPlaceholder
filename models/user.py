from pydantic import BaseModel, EmailStr


class Address(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str


class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    address: Address