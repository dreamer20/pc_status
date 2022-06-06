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