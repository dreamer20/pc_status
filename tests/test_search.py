import pytest


def test_index(client):
    """Get search page"""
    response = client.get('/search/')

    assert response.status_code == 200
    assert 'Поиск данных'.encode() in response.data


test_search_data = [
    ('2022-06-01', '2022-06-04', '2022.06.01</a> 00:00', '2022.06.04</a> 12:30'),
    ('2022-06-02', '2022-06-03', '2022.06.02</a> 00:00', '2022.06.03</a> 12:30'),
    ('', '', '2022.06.01</a> 00:00', '2022.06.04</a> 12:30'),
    ('2022-06-03', '2022-06-03', '2022.06.03</a> 00:00', '2022.06.03</a> 12:30'),
    ('', '2022-06-03', '2022.06.01</a> 00:00', '2022.06.03</a> 12:30'),
    ('2022-06-02', '', '2022.06.02</a> 00:00', '2022.06.04</a> 12:30')
]


@pytest.mark.parametrize(
    'from_date, to_date, start_datetime, stop_datetime', test_search_data)
def test_search_data(client, from_date, to_date, start_datetime, stop_datetime):
    """Check correctness of searching data in specific range of date"""
    params = {
        'from_date': from_date,
        'to_date': to_date
    }

    response = client.get('/search/', query_string=params)

    assert response.status_code == 200
    print(response.data.decode())
    assert start_datetime.encode() in response.data
    assert stop_datetime.encode() in response.data


def test_search_wrong_data_range(client):
    """Shows special message if range of dates is incorrect"""
    params = {
        'from_date': '2022-06-04',
        'to_date': '2022-06-02'
    }

    response = client.get('/search/', query_string=params)

    assert response.status_code == 200
    assert 'Выберите необходимый диапазон'.encode() in response.data
