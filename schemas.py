import pydantic
from pydantic import BaseModel
from datetime import datetime
from pydantic import EmailStr
from typing import Optional
from pydantic import BaseModel,Field, conint



class PostBased(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBased):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config:
        orm_mode = True

class Post(PostBased):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut
    
    class Config:
        orm_mode = True


class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    owner_id: int

    class Config:
        from_attributes = True
class PostOut(BaseModel):
    Post: PostResponse
    votes:int

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str



class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None


class Vote(BaseModel):
    post_id: int
    dir: int = Field(le=1, ge=0)
