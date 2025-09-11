# tests/test_stats.py
from datetime import date

import jwt

from app.models import Account, LogoAccess

ALGORITHM = "HS256"


def get_token(account):
    return jwt.encode({"usr": str(account.id)}, account.secret_key, algorithm=ALGORITHM)


def test_stats_endpoint(client):
    # создаём аккаунт
    acc = Account.create(name="B", inn="222", secret_key="k2")
    # создаём несколько записей с разными year и month
    LogoAccess.create(account=acc, year=2025, month=8, user=acc.id)
    LogoAccess.create(account=acc, year=2025, month=9, user=acc.id)
    LogoAccess.create(account=acc, year=2025, month=10, user=acc.id)

    token = get_token(acc)
    start = date(2025, 9, 1)
    end = date(2025, 10, 31)

    response = client.get(
        f"/stats?start={start}&end={end}", headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    # должны попасть только записи за 9 и 10 месяцы
    assert len(data) == 2
    months = [item["month"] for item in data]
    assert set(months) == {9, 10}
