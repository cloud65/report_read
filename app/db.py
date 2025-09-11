from uuid import uuid4

from peewee import Model, SqliteDatabase, UUIDField


class BaseModel(Model):
    id = UUIDField(primary_key=True, default=uuid4)


def init_db(models):
    db = SqliteDatabase("app.db")
    db.bind(models)
    db.connect()
    db.create_tables(models)
