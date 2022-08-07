from datetime import datetime


def timestamps_from_date_range(start_date, stop_date):

    try:
        start_timestamp = datetime.strptime(
            f'{start_date}T00:00:00', '%Y-%m-%dT%H:%M:%S').timestamp()
    except ValueError:
        start_timestamp = None

    try:
        stop_timestamp = datetime.strptime(
            f'{stop_date}T23:59:59', '%Y-%m-%dT%H:%M:%S').timestamp()
    except ValueError:
        stop_timestamp = None

    return (start_timestamp, stop_timestamp)


def get_new_offset(limit, offset, records_count):
    if offset == 0:
        previous_offset = None
    else:
        previous_offset = offset - limit
        if previous_offset < 0:
            previous_offset = 0
    next_offset = offset + limit
    if next_offset >= records_count:
        next_offset = None

    return previous_offset, next_offset
