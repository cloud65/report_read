import jwt

from app.settings import settings

ALGORITHM = "HS256"


def get_admin_token():
    return jwt.encode({"role": "admin"}, settings.admin_secret, algorithm=ALGORITHM)


def test_register_account(client):
    token = get_admin_token()
    response = client.post(
        "/accounts/register",
        json={"name": "Test Corp", "inn": "1234567890", "secret_key": "abc123"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Corp"
    assert data["inn"] == "1234567890"
    assert "id" in data
