import pc_status.db_api as db
from flask import (
    Blueprint, render_template, request
)


bp = Blueprint('search', __name__, url_prefix='/search')


@bp.route('/')
def index():
    from_date = request.args.get('from_date')
    to_date = request.args.get('to_date')
    limit = request.args.get('limit')
    offset = request.args.get('offset')

    if offset is None:
        offset = 0
    else:
        offset = int(offset)
    if limit is None:
        limit = 10
    else:
        limit = int(limit)

    result = db.get_records_by_range(from_date, to_date, limit, offset)
    offset = {
        'prev': result['previous_offset'],
        'next': result['next_offset']
    }
    date = {
        'from': result['from_date'],
        'to': result['to_date']
    }

    return render_template(
        'search.html',
        sys_info=result['records'],
        offset=offset,
        limit=limit,
        date=date
    )
