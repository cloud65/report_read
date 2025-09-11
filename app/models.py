from datetime import datetime

from peewee import CharField, DateTimeField, ForeignKeyField, IntegerField, UUIDField

from .db import BaseModel


class Account(BaseModel):
    secret_key = CharField(max_length=255)
    name = CharField(max_length=512)
    inn = CharField(max_length=12)


class LogoAccess(BaseModel):
    account = ForeignKeyField(Account, backref="accesses")
    year = IntegerField()
    month = IntegerField()
    user = UUIDField()
    first_access = DateTimeField(default=datetime.utcnow)
    last_access = DateTimeField(default=datetime.utcnow)

    class Meta:
        indexes = (
            (("account", "year", "month"), True),
            (("first_access",), False),
        )
