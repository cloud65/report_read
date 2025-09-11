from datetime import date
from typing import List

from fastapi import APIRouter, Depends, Query

from ..auth import get_current_account
from ..models import Account, LogoAccess
from ..schemas import LogoAccessSchema

router = APIRouter()


@router.get("/stats", response_model=List[LogoAccessSchema])
def get_stats(
    start: date = Query(...),
    end: date = Query(...),
    account: Account = Depends(get_current_account),
):
    start_val = start.year * 12 + start.month
    end_val = end.year * 12 + end.month

    query = (
        LogoAccess.select(
            LogoAccess.id,
            Account.id.alias("account"),
            LogoAccess.year,
            LogoAccess.month,
            LogoAccess.user,
            LogoAccess.first_access,
            LogoAccess.last_access,
        )
        .join(Account)  # явный join
        .where(
            (LogoAccess.account == account)
            & ((LogoAccess.year * 12 + LogoAccess.month).between(start_val, end_val))
        )
        .dicts()
    )

    return list(query)
