from typing import Optional

from pydantic import EmailStr, Field

from db.schemas import BaseModel


class AccountCreate(BaseModel):
    chat_id: int = Field(..., alias="id")
    first_name: str
    last_name: Optional[str] = None
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    is_legal_entity: bool = False
