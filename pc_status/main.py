from pc_status import db_api as db
from flask import (
    Blueprint, render_template, request
)

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    record = db.get_last_record()
    total_uptime = db.get_total_uptime()

    return render_template(
        'index.html',
        sys_info=record,
        total_uptime=total_uptime
    )


@bp.route('/add')
def add():
    sys_info = {
        'cpu_temp': request.args.get('cpu_temp'),
        'ssd_temp': request.args.get('ssd_temp'),
        'cpu_fan': request.args.get('cpu_fan'),
        'add_fan': request.args.get('add_fan'),
        'ram_total': request.args.get('ram_total'),
        'ram_available': request.args.get('ram_available'),
        'disk_space_total': request.args.get('disk_space_total'),
        'disk_space_available': request.args.get('disk_space_available'),
        'uptime': request.args.get('uptime'),
        'load_average': request.args.get('load_average'),
        'last_update': request.args.get('last_update'),
        'volume_level': request.args.get('volume_level'),
        'process_count': request.args.get('process_count'),
        'keyboard_layout': request.args.get('keyboard_layout')
    }

    total_uptime = request.args.get('total_uptime')

    if total_uptime.isnumeric():
        db.update_total_uptime(total_uptime)

    db.add(sys_info)

    return 'Successful.'
