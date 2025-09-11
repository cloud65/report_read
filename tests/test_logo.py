import os
import uuid


def test_logo_access(client):
    # Создаём аккаунт
    from app.models import Account

    acc = Account.create(name="A", inn="111", secret_key="k1")

    # Добавляем заглушку logo.png
    with open("logo.png", "wb") as f:
        f.write(b"fakeimage")

    url = f"/{acc.id}/2025/9/{uuid.uuid4()}/logo.png"
    response = client.get(url)
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"

    os.remove("logo.png")
