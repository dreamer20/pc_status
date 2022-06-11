import pytest
from datetime import datetime


empty_query_params = {
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

query_params = {
    'cpu_temp': 53.8,
    'ssd_temp': 34.9,
    'cpu_fan': 4078,
    'add_fan': 866,
    'ram_total': 16310072,
    'ram_available': 13250532,
    'disk_space_total': '29G',
    'disk_space_available': '9,1G',
    'uptime': '26',
    'load_average': ' 0,06 0,23 0,29',
    'last_update': '2022-06-06 20:42:44',
    'volume_level': 58,
    'process_count': 305,
    'keyboard_layout': 'us'
    }


def test_index(client):

    cur_datetime = datetime.fromtimestamp(1654345800.0).strftime("%Y.%m.%d %H:%M")

    response = client.get('/')

    assert response.status_code == 200
    assert cur_datetime.encode() in response.data


def test_add(client):

    response = client.get('/add', query_string=query_params)

    assert response.status_code == 200
    assert b'Successful.' in response.data

    response = client.get('/')

    assert response.status_code == 200
    assert b'13250532' in response.data
    assert b' 0,06 0,23 0,29' in response.data
    assert b'2022-06-06 20:42:44' in response.data


def test_add_empty_data(client):

    response = client.get('/add', query_string=empty_query_params)

    assert response.status_code == 200
    assert b'Successful.' in response.data

    response = client.get('/')

    assert response.status_code == 200
    assert b'-%' in response.data
    assert b'- GB / - GB' in response.data
    assert b'- PRM' in response.data
    assert b'-&#8451;' in response.data

def test_main_uptime_represention(client):

    query_string = dict(query_params)
    query_string['uptime'] = '2:22'

    response = client.get('/')
    
    assert '27 мин.'.encode() in response.data

    response = client.get('/add', query_string=query_string)

    assert response.status_code == 200
    assert b'Successful.' in response.data

    response = client.get('/')

    assert '2 ч. 22 мин.'.encode() in response.data

    query_string2 = dict(query_params)
    query_string2['uptime'] = '2'

    response = client.get('/add', query_string=query_string2)
    
    assert response.status_code == 200
    assert b'Successful.' in response.data

    response = client.get('/')

    assert '2 мин.'.encode() in response.data