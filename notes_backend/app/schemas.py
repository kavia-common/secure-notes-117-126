from pydantic import BaseModel, Field
from typing import List

# --- Auth-related schemas ---

# PUBLIC_INTERFACE
class UserSignup(BaseModel):
    username: str = Field(..., min_length=3, max_length=64, description="Username for signup")
    password: str = Field(..., min_length=6, max_length=128, description="Password for signup")

# PUBLIC_INTERFACE
class UserLogin(BaseModel):
    username: str = Field(..., min_length=3, max_length=64, description="Username for login")
    password: str = Field(..., min_length=6, max_length=128, description="Password for login")

# PUBLIC_INTERFACE
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

# --- Notes-related schemas ---

# PUBLIC_INTERFACE
class NoteBase(BaseModel):
    content: str = Field(..., description="Contents of the note")

# PUBLIC_INTERFACE
class NoteCreate(NoteBase):
    pass

# PUBLIC_INTERFACE
class NoteUpdate(BaseModel):
    content: str = Field(..., description="Updated content for the note")

# PUBLIC_INTERFACE
class NoteOut(NoteBase):
    id: int
    class Config:
        orm_mode = True

# PUBLIC_INTERFACE
class NotesList(BaseModel):
    notes: List[NoteOut]
