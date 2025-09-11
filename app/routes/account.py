from fastapi import APIRouter, Depends

from ..auth import verify_admin_jwt
from ..models import Account
from ..schemas import AccountCreateSchema, AccountSchema

router = APIRouter()


@router.post("/accounts/register", response_model=AccountSchema)
def register_account(data: AccountCreateSchema, _: str = Depends(verify_admin_jwt)):
    account = Account.create(name=data.name, inn=data.inn, secret_key=data.secret_key)
    return account
