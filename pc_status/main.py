import time
from datetime import datetime
from flask import (
    Blueprint, render_template, request, redirect, url_for
)
from pc_status.db import get_db


bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    db = get_db()
    sys_info = db.execute('SELECT * FROM pc_status WHERE cur_date = (SELECT max(cur_date) from pc_status)').fetchone()

    return render_template('index.html', sys_info=sys_info)


@bp.route('/add')
def add():
    cur_date = time.time()
    cpu_temp = request.args.get('cpu_temp')
    ssd_temp  = request.args.get('ssd_temp')
    cpu_fan  = request.args.get('cpu_fan')
    add_fan  = request.args.get('add_fan')
    ram_total  = request.args.get('ram_total')
    ram_available  = request.args.get('ram_available')
    disk_space_total  = request.args.get('disk_space_total')
    disk_space_available  = request.args.get('disk_space_available')
    uptime  = request.args.get('uptime')
    load_average  = request.args.get('load_average')
    last_update  = request.args.get('last_update')
    volume_level  = request.args.get('volume_level')
    process_count  = request.args.get('process_count')
    keyboard_layout  = request.args.get('keyboard_layout')

    sys_info = [
        cur_date,
        cpu_temp,
        ssd_temp,
        cpu_fan,
        add_fan,
        ram_total,
        ram_available,
        disk_space_total,
        disk_space_available,
        uptime,
        load_average,
        last_update,
        volume_level,
        process_count,
        keyboard_layout
    ]

    db = get_db()
    db.execute('''
        INSERT INTO pc_status (
            cur_date,
            cpu_temp,
            ssd_temp,
            cpu_fan,
            add_fan,
            ram_total,
            ram_available,
            disk_space_total,
            disk_space_available,
            uptime,
            load_average,
            last_update,
            volume_level,
            process_count,
            keyboard_layout) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', sys_info)
    db.commit()

    return 'Successful.'
