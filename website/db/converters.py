from returns.result import safe
from datetime import datetime, timezone

@safe
def to_float(x: str) -> float:
    return float(x)

@safe
def to_int(x: str) -> int:
    return int(x)

@safe
def to_datetime(x: str) -> datetime:
    local_datetime = datetime.fromisoformat(x)
    return local_datetime.astimezone(timezone.utc)

@safe
def to_bool(x: str) -> bool:
    if x == "on":
        return True
    else:
        return False
