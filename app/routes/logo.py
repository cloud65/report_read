# app/routes/logo.py
from datetime import datetime
from uuid import UUID

from fastapi import APIRouter, HTTPException, Path
from fastapi.responses import FileResponse

from ..models import Account, LogoAccess

router = APIRouter()


@router.get("/{account}/{year}/{month}/{user}/logo.png")
def get_logo(
    account: UUID = Path(...),
    year: int = Path(..., ge=2000, le=2100),
    month: int = Path(..., ge=1, le=12),
    user: UUID = Path(...),
):
    acc = Account.get_or_none(Account.id == account)
    if not acc:
        raise HTTPException(status_code=404, detail="Account not found")

    obj, created = LogoAccess.get_or_create(
        account=acc,
        year=year,
        month=month,
        user=user,
        defaults={"first_access": datetime.utcnow(), "last_access": datetime.utcnow()},
    )
    if not created:
        obj.last_access = datetime.utcnow()
        obj.save()

    headers = {"Cache-Control": "public, max-age=86400"}
    return FileResponse("logo.png", media_type="image/png", headers=headers)
