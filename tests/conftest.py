import os
import sys

import pytest
from fastapi.testclient import TestClient
from peewee import SqliteDatabase

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.models import Account, LogoAccess
from main import app


@pytest.fixture(autouse=True)
def setup_and_teardown_db():
    DATABASE = SqliteDatabase("app.db")
    DATABASE.init(":memory:")
    DATABASE.connect()
    DATABASE.create_tables([Account, LogoAccess])
    yield
    DATABASE.drop_tables([Account, LogoAccess])
    DATABASE.close()


@pytest.fixture
def client():
    return TestClient(app)
