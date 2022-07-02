from typing import Union
from datetime import datetime


def valueformat(value: Union[float, str]) -> Union[float, str]:
    if value == '':
        return '-'
    return value


def fromtimestamp(timestamp: float) -> str:
    return datetime.fromtimestamp(timestamp).strftime("%Y.%m.%d %H:%M")


def uptimeformat(time: str) -> str:
    if len(time) in (1, 2):
        return f'{time} мин.'
    elif len(time) > 2:
        _time = time.replace(':', ' ч. ')
        return f'{_time} мин.'
    else:
        return '-'
