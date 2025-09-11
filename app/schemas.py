# app/schemas.py
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class AccountSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    name: str
    inn: str
    secret_key: str


class AccountCreateSchema(BaseModel):
    name: str
    inn: str
    secret_key: str


class LogoAccessSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    account: UUID
    year: int
    month: int
    user: UUID
    first_access: datetime
    last_access: datetime
