from pc_status import db_api as db

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
    'load_average': '0,05 0,23 0,29',
    'last_update': '2022-06-06 20:42:44',
    'process_count': 303
}


def test_add_data(app_with_empty_db):
    ''' Adds new record to db '''
    with app_with_empty_db.app_context():
        record = db.add(test_data)

        assert record['cpu_temp'] == test_data['cpu_temp']
        assert record['uptime'] == test_data['uptime']
        assert record['load_average'] == test_data['load_average']


def test_get_last_recorded_data(app_with_empty_db):
    ''' Returns last added record '''
    test_data_2 = dict(test_data, cpu_temp=66, uptime='20')
    expected_data = dict(test_data, cpu_temp=88, uptime='33')

    with app_with_empty_db.app_context():
        db.add(test_data)
        record = db.get_last_record()

        assert record['cpu_temp'] == test_data['cpu_temp']
        assert record['uptime'] == test_data['uptime']
        assert record['load_average'] == test_data['load_average']

        db.add(test_data)
        db.add(test_data_2)
        db.add(expected_data)

        record = db.get_last_record()

        assert record['cpu_temp'] == expected_data['cpu_temp']
        assert record['uptime'] == expected_data['uptime']


def test_get_all_records(app_with_empty_db):
    ''' Returns all added records from db'''

    with app_with_empty_db.app_context():
        db.add(test_data)
        db.add(test_data)
        db.add(test_data)
        db.add(test_data)

        records = db.get_all_records()

        assert len(records) == 4
