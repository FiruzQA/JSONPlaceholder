from pydantic import BaseModel, EmailStr


class Comment(BaseModel):
    postId: int
    id: int
    name: str
    email: EmailStr
    body: str