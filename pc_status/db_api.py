from pc_status.db import get_db
import time


def add(data):
    cur_date = time.time()
    data_to_add = dict(data, cur_date=cur_date)
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
            process_count
        )
            VALUES (
                :cur_date,
                :cpu_temp,
                :ssd_temp,
                :cpu_fan,
                :add_fan,
                :ram_total,
                :ram_available,
                :disk_space_total,
                :disk_space_available,
                :uptime,
                :load_average,
                :last_update,
                :process_count
            )
    ''', data_to_add)
    db.commit()
    created_record = db.execute(
        'SELECT * FROM pc_status WHERE cur_date = ? ', (cur_date, )
    ).fetchone()

    return created_record


def get_last_record():
    db = get_db()
    record = db.execute(
        'SELECT * FROM pc_status WHERE cur_date =  \
        (SELECT max(cur_date) from pc_status)'
    ).fetchone()

    return record


def get_all_records():
    db = get_db()
    records = db.execute('SELECT * FROM pc_status').fetchall()

    return records


def get_total_uptime():
    db = get_db()
    record = db.execute('SELECT total_uptime FROM total_uptime').fetchone()

    return record['total_uptime']


def update_total_uptime(uptime):
    db = get_db()
    total_uptime = get_total_uptime()
    new_total_uptime = total_uptime + int(uptime)
    db.execute(
        'UPDATE total_uptime SET total_uptime = ? WHERE rowid = 1',
        (new_total_uptime, )
    )
    db.commit()

    return get_total_uptime()
