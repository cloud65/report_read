from uuid import UUID

import jwt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from .models import Account
from .settings import settings

ALGORITHM = "HS256"
auth_scheme = HTTPBearer()


def get_current_account(
    credentials: HTTPAuthorizationCredentials = Depends(auth_scheme),
) -> Account:
    token = credentials.credentials
    try:
        unverified_payload = jwt.decode(token, options={"verify_signature": False})
        account_id = UUID(unverified_payload["usr"])
        account = Account.get_or_none(Account.id == account_id)
        if not account:
            raise HTTPException(status_code=401, detail="Account not found")

        jwt.decode(token, account.secret_key, algorithms=[ALGORITHM])
        return account
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")


def verify_admin_jwt(credentials: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    token = credentials.credentials
    try:
        jwt.decode(token, settings.admin_secret, algorithms=[ALGORITHM])
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid admin token")
