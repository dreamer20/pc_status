from datetime import datetime, timedelta
from flask import (
    Blueprint, render_template, request, redirect, url_for
)
from pc_status.db import get_db


bp = Blueprint('search', __name__, url_prefix='/search')


@bp.app_template_filter()
def fromtimestamp(timestamp):
    return datetime.fromtimestamp(timestamp).strftime("%Y.%m.%d %H:%M")


@bp.route('/')
def index():
    db = get_db()
    start = None
    stop = None
    from_date = request.args.get('from_date')
    to_date = request.args.get('to_date')

    if from_date is not None and from_date != '':
        start = datetime.strptime(f'{from_date}T00:00:00', '%Y-%m-%dT%H:%M:%S').timestamp()
    if to_date is not None and to_date != '':
        to_date = datetime.strptime(to_date, '%Y-%m-%d') + timedelta(days=1)
        stop = to_date.timestamp()

    if start is None and stop is not None:
        data = db.execute("SELECT * from pc_status where cur_date <= ?", (stop,)).fetchall()
    elif start is not None and stop is None:
        data = db.execute("SELECT * from pc_status where cur_date >= ?", (start,)).fetchall()
    elif start is not None and stop is not None:
        data = db.execute("SELECT * from pc_status where cur_date >= ? and cur_date <= ? order by cur_date", (start, stop)).fetchall()
    else:
        data = db.execute("SELECT * from pc_status order by cur_date").fetchall()

    return render_template('search.html', sys_info=data)
