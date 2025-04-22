from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    user_name: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    user_name: str
    
    class Config:
        orm_mode = True
