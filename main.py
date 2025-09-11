from fastapi import FastAPI

from app.db import init_db
from app.models import Account, LogoAccess
from app.routes import account, logo, stats

app = FastAPI()

# Инициализация базы
init_db([Account, LogoAccess])

# Подключение роутеров
app.include_router(logo.router)
app.include_router(stats.router)
app.include_router(account.router)
