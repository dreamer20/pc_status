from typing import Union
from datetime import datetime, timedelta


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


def totaluptimeformat(uptime: int) -> str:
    if uptime < 60:
        return 'меньше минуты'
    tdelta = timedelta(seconds=uptime)
    hours, minutes = 0, 0
    totaluptime_string = ''

    if tdelta.seconds >= 3600:
        hours = tdelta.seconds // 3600
        minutes = (tdelta.seconds % 3600) // 60
    else:
        minutes = tdelta.seconds // 60

    if (tdelta.days > 0):
        totaluptime_string = f'{tdelta.days} д. '

    if (hours > 0):
        totaluptime_string += f'{hours} ч. '

    if (minutes > 0):
        if len(str(minutes)) == 1:
            totaluptime_string += f'0{minutes} мин.'
        else:
            totaluptime_string += f'{minutes} мин.'

    return totaluptime_string
