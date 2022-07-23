from pc_status.db import get_db

test_data = {
    'cpu_temp': 50.8,
    'ssd_temp': 22.9,
    'cpu_fan': 4000,
    'add_fan': 800,
    'ram_total': 16310072,
    'ram_available': 13250532,
    'disk_space_total': '29G',
    'disk_space_available': '9,1G',
    'uptime': '26',
    'load_average': ' 0,05 0,23 0,29',
    'last_update': '2022-06-06 20:42:44',
    'volume_level': 59,
    'process_count': 303,
    'keyboard_layout': 'us'
}

test_data_empty = {
    'cpu_temp': '',
    'ssd_temp': '',
    'cpu_fan': '',
    'add_fan': '',
    'ram_total': '',
    'ram_available': '',
    'disk_space_total': '',
    'disk_space_available': '',
    'uptime': '',
    'load_average': '',
    'last_update': '',
    'volume_level': '',
    'process_count': '',
    'keyboard_layout': ''
}


def test_db(app):
    """ Returns the same db for app """
    with app.app_context():
        db = get_db()
        assert db is get_db()


def test_add_data(client, app):
    """ Adds new record to db """
    response = client.get('/add', query_string=test_data)

    assert response.status_code == 200
    assert b'Successful.' in response.data

    with app.app_context():
        db = get_db()
        sys_info = db.execute('SELECT * FROM pc_status WHERE cur_date = \
                          (SELECT max(cur_date) from pc_status)').fetchone()
        assert sys_info['cpu_temp'] == test_data['cpu_temp']
        assert sys_info['ssd_temp'] == test_data['ssd_temp']
        assert sys_info['cpu_fan'] == test_data['cpu_fan']
        assert sys_info['add_fan'] == test_data['add_fan']
        assert sys_info['ram_total'] == test_data['ram_total']
        assert sys_info['ram_available'] == test_data['ram_available']
        assert sys_info['disk_space_total'] == test_data['disk_space_total']
        assert sys_info['disk_space_available'] == test_data['disk_space_available']
        assert sys_info['uptime'] == test_data['uptime']
        assert sys_info['load_average'] == test_data['load_average']
        assert sys_info['last_update'] == test_data['last_update']
        assert sys_info['volume_level'] == test_data['volume_level']
        assert sys_info['process_count'] == test_data['process_count']
        assert sys_info['keyboard_layout'] == test_data['keyboard_layout']


def test_add_empty_data(client, app):
    """ Adds empty data to db """
    response = client.get('/add', query_string=test_data_empty)

    assert response.status_code == 200
    assert b'Successful.' in response.data

    with app.app_context():
        db = get_db()
        sys_info = db.execute('SELECT * FROM pc_status WHERE cur_date = \
                          (SELECT max(cur_date) from pc_status)').fetchone()
        assert sys_info['cpu_temp'] == ''
        assert sys_info['ssd_temp'] == ''
        assert sys_info['cpu_fan'] == ''
        assert sys_info['add_fan'] == ''
        assert sys_info['ram_total'] == ''
        assert sys_info['ram_available'] == ''
        assert sys_info['disk_space_total'] == ''
        assert sys_info['disk_space_available'] == ''
        assert sys_info['uptime'] == ''
        assert sys_info['load_average'] == ''
        assert sys_info['last_update'] == ''
        assert sys_info['volume_level'] == ''
        assert sys_info['process_count'] == ''
        assert sys_info['keyboard_layout'] == ''
